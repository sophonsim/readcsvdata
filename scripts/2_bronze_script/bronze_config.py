layer = "bronze"
source_crm = "source_crm"
source_erp = "source_erp"

BRONZE_CONFIG = [
    # source crm 
    {
        "file" : "cust_info",
        "path" : f"/Volumes/readcsvdata/{layer}/{source_crm}",
        "format" : "csv",
        "table_path" : f"readcsvdata.{layer}",
        "table" : f"{layer}_crm_cust_info"
    },
    {
        "file" : "prd_info",
        "path" : f"/Volumes/readcsvdata/{layer}/{source_crm}",
        "format" : "csv",
        "table_path" : f"readcsvdata.{layer}",
        "table" : f"{layer}_crm_prd_info"
    },
    {
        "file" : "sales_details",
        "path" : f"/Volumes/readcsvdata/{layer}/{source_crm}",
        "format" : "csv",
        "table_path" : f"readcsvdata.{layer}",
        "table" : f"{layer}_crm_sales_details"
    },

    # sourc erp
        {
        "file" : "CUST_AZ12",
        "path" : f"/Volumes/readcsvdata/{layer}/{source_erp}",
        "format" : "csv",
        "table_path" : f"readcsvdata.{layer}",
        "table" : f"{layer}_erp_cust_az12"
    },
    {
        "file" : "LOC_A101",
        "path" : f"/Volumes/readcsvdata/{layer}/{source_erp}",
        "format" : "csv",
        "table_path" : f"readcsvdata.{layer}",
        "table" : f"{layer}_erp_loc_a101"
    },
    {
        "file" : "PX_CAT_G1V2",
        "path" : f"/Volumes/readcsvdata/{layer}/{source_erp}",
        "format" : "csv",
        "table_path" : f"readcsvdata.{layer}",
        "table" : f"{layer}_erp_px_cat_g1v2"
    }
]