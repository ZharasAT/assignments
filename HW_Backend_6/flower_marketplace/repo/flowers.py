from models.flower import Flower
from typing import List

class FlowersRepository:
    flowers: List[Flower] = []

    @classmethod
    def add_flower(cls, flower: Flower):
        """Adding of a new flower to repository"""
        cls.flowers.append(flower)

    @classmethod
    def get_all_flowers(cls) -> List[Flower]:
        """Getting of all flowers"""
        return cls.flowers

    @classmethod
    def get_flower_by_id(cls, id: int) -> Flower | None:
        return next((flower for flower in cls.flowers if flower.id == id), None)
