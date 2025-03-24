from models.purchase import Purchase
from typing import List

class PurchasesRepository:
    purchases: List[Purchase] = []

    @classmethod
    def add_purchase(cls, user_id: int, flower_ids: List[int]):
        """Add a single purchase"""
        for flower_id in flower_ids:
            cls.purchases.append(Purchase(user_id=user_id, flower_id=flower_id))

    @classmethod
    def add_purchases(cls, user_id: int, flower_ids: List[int]):
        """Add multiple purchases"""

    @classmethod
    def get_purchases_by_user(cls, user_id: int) -> List[Purchase]:
        """Getting of all purchases of the user"""
        return [purchase for purchase in cls.purchases if purchase.user_id == user_id]