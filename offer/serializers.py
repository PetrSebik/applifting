from rest_framework import serializers
from applifting.offer.models import Offer
from applifting.product.models import Product


class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = (
            "id",
            "price",
            "items_in_stock",

        )
        read_only_fields = (
            "id",
        )


class ProductOffersSerializer(serializers.ModelSerializer):
    offers = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "offers",
        )
        read_only_fields = (
            "id",
            "offers",
        )

    def get_offers(self, instance):
        return OfferSerializer(instance.offers, many=True, context=self.context).data
