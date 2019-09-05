from typing import List

from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get("")
def read_items():
    """
    Retrieve items.
    """
    pass


@router.post("")
def create_item():
    """
    Create new item.
    """
    pass


@router.put("/{id}")
def update_item():
    """
    Update an item.
    """
    pass


@router.get("/{id}")
def read_user_me():
    """
    Get item by ID.
    """
    pass


@router.delete("/{id}")
def delete_item():
    """
    Delete an item.
    """
    pass
