layer = "bronze"
path = f"/Volumes/readcsvdata"
desination = ["landing_source_crm","landing_source_erp","process_source_crm","process_source_erp"]



BRONZE_CONFIG = [
    # source crm 
    {
        "file" : "cust_info",
        "path_land" : f"{path}/{layer}/{desination[0]}",
        "format" : "csv",
        "table_path" : f"readcsvdata.{layer}",
        "table" : f"{layer}_crm_cust_info",
        "path_processed" : f"{path}/{layer}/{desination[2]}"
    },
    {
        "file" : "prd_info",
        "path_land" : f"{path}/{layer}/{desination[0]}",
        "format" : "csv",
        "table_path" : f"readcsvdata.{layer}",
        "table" : f"{layer}_crm_prd_info",
        "path_processed" : f"{path}/{layer}/{desination[2]}"
    },
    {
        "file" : "sales_details",
        "path_land" : f"{path}/{layer}/{desination[0]}",
        "format" : "csv",
        "table_path" : f"readcsvdata.{layer}",
        "table" : f"{layer}_crm_sales_details",
        "path_processed" : f"{path}/{layer}/{desination[2]}"
    },

    # sourc erp
        {
        "file" : "CUST_AZ12",
        "path_land" : f"{path}/{layer}/{desination[1]}",
        "format" : "csv",
        "table_path" : f"readcsvdata.{layer}",
        "table" : f"{layer}_erp_cust_az12",
        "path_processed" : f"{path}/{layer}/{desination[3]}"
    },
    {
        "file" : "LOC_A101",
        "path_land" : f"{path}/{layer}/{desination[1]}",
        "format" : "csv",
        "table_path" : f"readcsvdata.{layer}",
        "table" : f"{layer}_erp_loc_a101",
        "path_processed" : f"{path}/{layer}/{desination[3]}"
    },
    {
        "file" : "PX_CAT_G1V2",
        "path_land" : f"{path}/{layer}/{desination[1]}",
        "format" : "csv",
        "table_path" : f"readcsvdata.{layer}",
        "table" : f"{layer}_erp_px_cat_g1v2",
        "path_processed" : f"{path}/{layer}/{desination[3]}"
    }
]