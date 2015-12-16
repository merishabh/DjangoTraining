from rest_framework import serializers
from ecom_module.models import Category, Item, Cart


class CategorySerializers(serializers.ModelSerializer):
    """
    Serializer for category.
    """
    class Meta:
        model = Category
        fields = ('name', 'description', 'parent')

    def create(self, validated_data):
        """
        """
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class ItemSerializers(serializers.ModelSerializer):
    """
    Serializer for Items.
    """
    class Meta:
        model = Item
        fields = ('subcategory', 'category', 'name', 'brand', 'specification', 'price')

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.brand = validated_data.get('brand',instance.brand)
        instance.specification = validated_data.get('specification', instance.specification)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class CartSerializers(serializers.ModelSerializer):
    """
    Serializer for cart.
    """
    class Meta:
        model = Cart
        fields = ('owner', 'item', 'quantity', 'total_price')

    def create(self, validated_data):
        """
        """
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.brand = validated_data.get('item',instance.item)
        instance.quantity = validated_data.get('quatity', instance.quantity)
        instance.total_price = validated_data.get('total_price', instance.total_price)
        instance.save()
        return instance









