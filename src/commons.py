import os

DATA_SOURCE = os.path.abspath("../data/car_loan_trainset_clean.csv")
DB_NAME = "cars"
SCHEMA_NAME = "loans"
TABLE_NAME = "car_loan"
API_TABLE_NAME = "api_predictions"
TARGET = "loan_default"

MODEL_PATH = os.path.abspath("../models/classifier.pkl")

FEATURES = [
    # "customer_id",
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

TEST_SAMPLE = {
    # "customer_id": 75675.0,
    "main_account_loan_no": 1.0,
    "main_account_active_loan_no": 0.0,
    "main_account_overdue_no": 0.0,
    "main_account_outstanding_loan": 0.0,
    "main_account_sanction_loan": 0.0,
    "main_account_disbursed_loan": 0.0,
    "sub_account_loan_no": 0.0,
    "sub_account_active_loan_no": 0.0,
    "sub_account_overdue_no": 0.0,
    "sub_account_outstanding_loan": 0.0,
    "sub_account_sanction_loan": 0.0,
    "sub_account_disbursed_loan": 0.0,
    "disbursed_amount": 36179.0,
    "asset_cost": 48114.0,
    "branch_id": 37.0,
    "supplier_id": 613.0,
    "manufacturer_id": 4.0,
    "area_id": 2.0,
    "employee_code_id": 2255.0,
    "mobileno_flag": 1.0,
    "idcard_flag": 1.0,
    "Driving_flag": 0.0,
    "passport_flag": 0.0,
    "credit_score": 17.0,
    "main_account_monthly_payment": 0.0,
    "sub_account_monthly_payment": 0.0,
    "last_six_month_new_loan_no": 0.0,
    "last_six_month_defaulted_no": 0.0,
    "average_age": 2.0,
    "credit_history": 2.0,
    "enquirie_no": 0.0,
    "loan_to_asset_ratio": 0.751943301,
    "total_account_loan_no": 1.0,
    "sub_account_inactive_loan_no": 1.0,
    "total_inactive_loan_no": 0.0,
    "main_account_inactive_loan_no": 1.0,
    "total_overdue_no": 0.0,
    "total_outstanding_loan": 0.0,
    "total_sanction_loan": 0.0,
    "total_disbursed_loan": 0.0,
    "total_monthly_payment": 0.0,
    "outstanding_disburse_ratio": 1.0,
    "main_account_tenure": 0.0,
    "sub_account_tenure": 0.0,
    "disburse_to_sactioned_ratio": 1.0,
    "active_to_inactive_act_ratio": 1.0,
    "year_of_birth": 1987.0,
    "disbursed_date": 2019.0,
    "Credit_level": -1.0,
    "employment_type": 0.0,
    "age": 32.0,
}
