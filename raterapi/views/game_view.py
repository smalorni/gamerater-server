# Handles game requests
from urllib import response
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterapi.models import Game, Review, Category

class GameView(ViewSet):
    """GameRater View"""

    def list(self, request):
        """Handles GET requests to get all games
           Returns: Response --JSON serialized list of games"""

        games = Game.objects.all()
        # Might need to loop through here ******
        
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """Handles GET requests for single game
           Returns: Response --JSON serializes game"""
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data)
        # Responds with 404 message if game doesn't exist
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request):
        """Handles POST operations
           Returns: Response --JSON serializes game instance"""
        # We use player here
        #player = Player.objects.get(user=request.auth.user)
        #category = Category.objects.get(pk=request.data[]) #Need to figure out what goes in here ****
