import pandas as pd

from .schema_config import SCHEMA_WHITELIST


def transform(databases: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
    normalized_databases = normalize_df(databases)
    filter_whitelist_cols(normalized_databases)
    return normalized_databases


def normalize_df(
    databases: dict[str, pd.DataFrame],
) -> dict[str, pd.DataFrame]:
    for df in databases.values():
        df.columns = df.columns.str.lower().str.replace(" ", "_")
        string_df = df.select_dtypes(include=str)
        for col in string_df.columns:
            df[col] = string_df[col].str.lower().str.replace(" ", "_")

    # Fun row-wise version
    # num_rows = df.index.stop
    # for i in range(num_rows):
    #     row = df.iloc[i]
    #     df.iloc[i] = row.map(
    #         lambda x: x.lower().replace(" ", "_") if isinstance(x, str) else x
    #     )
    #     print(df.iloc[i])
    return databases


# These columns are not relevant to analysis. Must remove them to fit the
# schemas defined on supabase.
def filter_whitelist_cols(
    normalized_databases: dict[str, pd.DataFrame],
) -> None:
    for db, df in normalized_databases.items():
        normalized_databases[db] = df[list(SCHEMA_WHITELIST[db])]
