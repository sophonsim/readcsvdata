import initial_config as ic
import importlib

importlib.reload(ic)

# github base url
github_url = "https://raw.githubusercontent.com/sophonsim/readcsvdata/refs/heads/main/dataset/source"
target = f"/Volumes/{ic.catalog_setup}/{ic.schema_setup[0]}/landing"
processed = f"/Volumes/{ic.catalog_setup}/{ic.schema_setup[0]}/processed"

# source data copy
SOURCE_CONFIG = [
    {
        "url" : f"{ic.github_url}/{ic.volume_setup[0]}/cust_info.csv",
        "target" : f"{ic.target}/{ic.volume_setup[0]}/cust_info.csv",
        "processed" : f"{ic.processed}/{ic.volume_setup[0]}/cust_info.csv"
    },
    {
        "url" : f"{ic.github_url}/{ic.volume_setup[0]}/prd_info.csv",
        "target" : f"{ic.target}/{ic.volume_setup[0]}/prd_info.csv"
    },
    {
        "url" : f"{ic.github_url}/{ic.volume_setup[0]}/sales_details.csv",
        "target" : f"{ic.target}/{ic.volume_setup[0]}/sales_details.csv"
    },
    {
        "url" : f"{ic.github_url}/{ic.volume_setup[1]}/CUST_AZ12.csv",
        "target" : f"{ic.target}/{ic.volume_setup[1]}/CUST_AZ12.csv"
    },
    {
        "url" : f"{ic.github_url}/{ic.volume_setup[1]}/LOC_A101.csv",
        "target" : f"{ic.target}/{ic.volume_setup[1]}/LOC_A101.csv"
    },
     {
        "url" : f"{ic.github_url}/{ic.volume_setup[1]}/PX_CAT_G1V2.csv",
        "target" : f"{ic.target}/{ic.volume_setup[1]}/PX_CAT_G1V2.csv"
    }
    
]
