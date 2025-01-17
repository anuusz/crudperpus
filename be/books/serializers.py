from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
    def validate(self, data):
        print("Data diterima:", data)  # Debug data
        return data
