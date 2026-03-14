# project environment setup parameter
catalog_setup = "readcsvdata"
schema_setup = ["bronze", "silver", "gold"]
volume_setup = ["landing_source_crm", "landing_source_erp","process_source_crm", "process_source_erp"]


# github base url
github_url = "https://raw.githubusercontent.com/sophonsim/readcsvdata/refs/heads/main/dataset/source"
github_source = ["source_crm","source_erp"]
target = f"/Volumes/{catalog_setup}/{schema_setup[0]}"
processed = f"/Volumes/{catalog_setup}/{schema_setup[0]}"

# source data copy
SOURCE_CONFIG = [
    {
        "url" : f"{github_url}/{github_source[0]}/cust_info.csv",
        "target" : f"{target}/{volume_setup[0]}/cust_info.csv"
    },
    {
        "url" : f"{github_url}/{github_source[0]}/prd_info.csv",
        "target" : f"{target}/{volume_setup[0]}/prd_info.csv"
    },
    {
        "url" : f"{github_url}/{github_source[0]}/sales_details.csv",
        "target" : f"{target}/{volume_setup[0]}/sales_details.csv"
    },
    {
        "url" : f"{github_url}/{github_source[1]}/CUST_AZ12.csv",
        "target" : f"{target}/{volume_setup[1]}/CUST_AZ12.csv"
    },
    {
        "url" : f"{github_url}/{github_source[1]}/LOC_A101.csv",
        "target" : f"{target}/{volume_setup[1]}/LOC_A101.csv"
    },
     {
        "url" : f"{github_url}/{github_source[1]}/PX_CAT_G1V2.csv",
        "target" : f"{target}/{volume_setup[1]}/PX_CAT_G1V2.csv"
    }
    
]

