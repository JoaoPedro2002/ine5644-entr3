import pandas as pd


class DataWrapper:
    def __init__(self):
        self.__dataframes = {}

    @property
    def customers(self) -> pd.DataFrame:
        if "customers" not in self.__dataframes:
            self.__dataframes["customers"] = pd.read_csv('data/olist_customers_dataset.csv')
        return self.__dataframes["customers"]

    @property
    def geolocation(self) -> pd.DataFrame:
        if "geolocation" not in self.__dataframes:
            self.__dataframes["geolocation"] = pd.read_csv('data/olist_geolocation_dataset.csv')
        return self.__dataframes["geolocation"]

    @property
    def order_items(self) -> pd.DataFrame:
        if "order_items" not in self.__dataframes:
            self.__dataframes["order_items"] = pd.read_csv('data/olist_order_items_dataset.csv')
        return self.__dataframes["order_items"]

    @property
    def order_payments(self) -> pd.DataFrame:
        if "order_payments" not in self.__dataframes:
            self.__dataframes["order_payments"] = pd.read_csv('data/olist_order_payments_dataset.csv')
        return self.__dataframes["order_payments"]

    @property
    def order_reviews(self) -> pd.DataFrame:
        if "order_reviews" not in self.__dataframes:
            self.__dataframes["order_reviews"] = pd.read_csv('data/olist_order_reviews_dataset.csv')
        return self.__dataframes["order_reviews"]

    @property
    def orders(self) -> pd.DataFrame:
        if "orders" not in self.__dataframes:
            self.__dataframes["orders"] = pd.read_csv('data/olist_orders_dataset.csv')
        return self.__dataframes["orders"]

    @property
    def products(self) -> pd.DataFrame:
        if "products" not in self.__dataframes:
            self.__dataframes["products"] = pd.read_csv('data/olist_products_dataset.csv')
        return self.__dataframes["products"]

    @property
    def sellers(self) -> pd.DataFrame:
        if "sellers" not in self.__dataframes:
            self.__dataframes["sellers"] = pd.read_csv('data/olist_sellers_dataset.csv')
        return self.__dataframes["sellers"]

    @property
    def product_category_name_translation(self) -> pd.DataFrame:
        if "product_category_name_translation" not in self.__dataframes:
            self.__dataframes["product_category_name_translation"] = pd.read_csv('data/product_category_name_translation.csv')
        return self.__dataframes["product_category_name_translation"]