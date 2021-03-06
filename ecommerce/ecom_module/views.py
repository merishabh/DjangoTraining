from django.shortcuts import render
from django.http import Http404
from django.http import JsonResponse

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import generics
from rest_framework import status
import json

from ecom_module.models import Category, Item, Cart
from ecom_module.serializers import CategorySerializers, ItemSerializers, CartSerializers


class AddItem(APIView):
    """
    Allows the user to add items under given subcategory or category.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ecom_module/addItem.html'

    def get(self, request):
        """
        gets the added items.
        """
        category = Category.objects.all()
        category_list = []
        subcategory_list = []
        data = {}
        for categ in category:
            if categ.parent is None:
                data['id'] = categ.id
                data['name'] = str(categ.name)
                data['description'] = str(categ.description)
                category_list.append(data)
                data = {}
            else:
                data['id'] = categ.id
                data['name'] = str(categ.name)
                data['description'] = str(categ.description)
                data['parent'] = categ.parent.id
                subcategory_list.append(data)
                data = {}
        return render(request,'ecom_module/addItem.html',
                      {'category': category_list, 'subcategory': subcategory_list})

    def post(self, request):
        """
        post the item added by the user to the model.
        """
        serializer = ItemSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(Item.objects.all())
            return JsonResponse({'success': 'You have successfully saved item'})
        return JsonResponse({'failure': 'Unsuccessful in saving item'})


class AddCategory(APIView):
    """
    Allows the user to add category and subcategory.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ecom_module/addCategory.html'

    def get(self, request):
        """
        renders the addCategory html file
        """
        category = Category.objects.all()
        category_list = []
        data = {}
        for categ in category:
            if categ.parent is None:
                data['id'] = categ.id
                data['name'] = str(categ.name)
                category_list.append(data)
                data = {}
        return render(request,'ecom_module/addCategory.html',
                      {'category': category_list})

    def post(self, request):
        """
        post added data to server.
        """
        serializer = CategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': 'You have successfully added the category'})
        return JsonResponse({'failure': 'Unsuccessful in adding category'})


class DeleteCategory(APIView):
    """

    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ecom_module/deleteCategory.html'

    def get(self, request):
        """
        renders the deleteCategory html file
        """
        category = Category.objects.all()
        category_list = []
        data = {}
        for categ in category:
            if categ.parent is None:
                data['id'] = categ.id
                data['name'] = str(categ.name)
                category_list.append(data)
                data = {}
        return render(request,'ecom_module/deleteCategory.html',
                      {'category': category_list})

    def post(self, request):
        """
        post added data to server.
        """
        serializer = Category.objects.get(pk=request.POST['id'])
        serializer.delete()
        return JsonResponse({'success': 'You have successfully deleted item', 'failure': 'Unsuccessful in deleting item'})




class CategoryList(APIView):
    """
    Displays all the categories.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ecom_module/index.html'

    def get(self, request):
        """
        renders the ecom_module html file.
        """
        category = Category.objects.all()
        subcategory_list = []
        category_list = []
        for cat in category:
            if cat.parent is not None:
                subcategory_list.append(cat)
            else:
                category_list.append(cat)
        return Response({'subcategory': subcategory_list, 'category': category_list})


class CategoryDetail(APIView):
    """
    Details of the particular category is displayed
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ecom_module/categoryDetail.html'

    def get_object(self, pk):
        """
        get the category object of the given pk.
        """
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        renders the categoryDetail html file.
        """
        category = self.get_object(pk)
        serializer = CategorySerializers(category)
        return Response({'serializer': serializer, 'category': category})


class ItemList(APIView):
    """
    Displays the item list
    """

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ecom_module/itemList.html'

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        sub_category = self.get_object(pk)
        items = Item.objects.all()
        item_list = []
        data = {}
        for item in items:
            if item.subcategory.id == sub_category.id:
                data['id'] = item.id
                data['name'] = str(item.name)
                data['brand'] = str(item.brand)
                item_list.append(data)
                data = {}
        return Response({'items': item_list})


class ItemDetail(APIView):
    """
    Displays details of the given item.
    """

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ecom_module/itemDetail.html'

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializers(item)
        return Response({'serializer': serializer, 'item': item})


class CartList(APIView):
    """
    Displays cart list.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ecom_module/cartDetail.html'

    def post(self, request, format=None):
        serializer = CartSerializers(request)
        return Response({'serializer': serializer, 'cart': request.body})


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Displays cart details.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializers




