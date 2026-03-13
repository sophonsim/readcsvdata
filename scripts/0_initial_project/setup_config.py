# project environment setup parameter
catalog_setup = "readcsvdata"
schema_setup = ["bronze", "silver", "gold"]
volume_setup = ["source_crm", "source_erp"]

# github base url
github_url = "https://raw.githubusercontent.com/sophonsim/readcsvdata/refs/heads/main/dataset/source/"

# source data copy
SOURCE_CONFIG = [
    {
        "url" : f"{github_url}/source_crm/cust_info.csv$0",
        "target" : f"/Volumes/{catalog_setup}/bronze/source_crm/cust_info.csv"
    },
    {
        "url" : f"{github_url}/source_crm/prd_info.csv$0",
        "target" : f"/Volumes/{catalog_setup}/bronze/source_crm/prd_info.csv"
    },
    {
        "url" : f"{github_url}/source_crm/sales_details.csv$0",
        "target" : f"/Volumes/{catalog_setup}/bronze/source_crm/sales_details.csv"
    },
    {
        "url" : f"{github_url}/source_erp/CUST_AZ12.csv$0",
        "target" : f"/Volumes/{catalog_setup}/bronze/source_erp/CUST_AZ12.csv"
    },
    {
        "url" : f"{github_url}/source_erp/LOC_A101.csv$0",
        "target" : f"/Volumes/{catalog_setup}/bronze/source_er/LOC_A101.csv"
    },
     {
        "url" : f"{github_url}/source_erp/PX_CAT_G1V2.csv$0",
        "target" : f"/Volumes/{catalog_setup}/bronze/source_erp/PX_CAT_G1V2.csv"
    }
    
]


