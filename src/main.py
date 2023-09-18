import matplotlib.pyplot as plt

from src.data_preparation import binarize_column, map_column, merge_dataframes
from src.data_wrapper import DataWrapper

if __name__ == "__main__":
    data_wrapper = DataWrapper()

    binarization_geo: dict[str, dict] = binarize_column(data_wrapper.geolocation, ["geolocation_state", "geolocation_city"])

    map_column(data_wrapper.customers, "customer_state", binarization_geo["geolocation_state"], int)
    map_column(data_wrapper.customers, "customer_city", binarization_geo["geolocation_city"], int)

    map_column(data_wrapper.sellers, "seller_state", binarization_geo["geolocation_state"], int)
    map_column(data_wrapper.sellers, "seller_city", binarization_geo["geolocation_city"], int)

    binarization_payments: dict[str, dict] = binarize_column(data_wrapper.order_payments, ["payment_type"])

    merged = merge_dataframes(data_wrapper.orders, data_wrapper.customers, "customer_id")
    print(merged)

    plt.show()





