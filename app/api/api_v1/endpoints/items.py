from typing import List

from fastapi import APIRouter, Depends, HTTPException

from models.item import Item, ItemCreate, ItemUpdate

router = APIRouter()


@router.get("", response_model=List[Item])
def read_items():
    """
    Retrieve items.
    """
    pass


@router.post("", response_model=Item)
def create_item(*,
    item_in: ItemCreate,
):
    """
    Create new item.
    """
    pass


@router.put("/{id}",response_model=Item)
def update_item(*,
    item_in: ItemUpdate,
):
    """
    Update an item.
    """
    pass


@router.get("/{id}", response_model=Item)
def read_user_me():
    """
    Get item by ID.
    """
    pass


@router.delete("/{id}", response_model=Item)
def delete_item():
    """
    Delete an item.
    """
    pass
