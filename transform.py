import pandas as pd


def transform(databases: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
    for df in databases.values():
        normalize_df(df)
        delete_df_cols(df)
    return databases


def normalize_df(df: pd.DataFrame) -> None:
    df.columns = (
        df.columns.str.replace("- ", "").str.replace(" ", "_").str.lower()
    )
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


def delete_df_cols(df: pd.DataFrame) -> None:
    return None
