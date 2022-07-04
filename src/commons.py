import os

DATA_SOURCE = "./data/car_loan_trainset_clean.csv"
DB_NAME = "cars"
SCHEMA_NAME = "loans"
TABLE_NAME = "car_loan"
TARGET = "loan_default"

MODEL_PATH = os.path.abspath("../models/classifier.pkl")

FEATURES = [
    "customer_id",
    "main_account_loan_no",
    "main_account_active_loan_no",
    "main_account_overdue_no",
    "main_account_outstanding_loan",
    "main_account_sanction_loan",
    "main_account_disbursed_loan",
    "sub_account_loan_no",
    "sub_account_active_loan_no",
    "sub_account_overdue_no",
    "sub_account_outstanding_loan",
    "sub_account_sanction_loan",
    "sub_account_disbursed_loan",
    "disbursed_amount",
    "asset_cost",
    "branch_id",
    "supplier_id",
    "manufacturer_id",
    "area_id",
    "employee_code_id",
    "mobileno_flag",
    "idcard_flag",
    "Driving_flag",
    "passport_flag",
    "credit_score",
    "main_account_monthly_payment",
    "sub_account_monthly_payment",
    "last_six_month_new_loan_no",
    "last_six_month_defaulted_no",
    "average_age",
    "credit_history",
    "enquirie_no",
    "loan_to_asset_ratio",
    "total_account_loan_no",
    "sub_account_inactive_loan_no",
    "total_inactive_loan_no",
    "main_account_inactive_loan_no",
    "total_overdue_no",
    "total_outstanding_loan",
    "total_sanction_loan",
    "total_disbursed_loan",
    "total_monthly_payment",
    "outstanding_disburse_ratio",
    "main_account_tenure",
    "sub_account_tenure",
    "disburse_to_sactioned_ratio",
    "active_to_inactive_act_ratio",
    "year_of_birth",
    "disbursed_date",
    "Credit_level",
    "employment_type",
    "age",
]
