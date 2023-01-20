from uuid import uuid1
import random
from flask_socketio import join_room
class Rooms:
    def __init__(self,num_rooms=5,namespace="Rooms"):
        self.num_rooms = num_rooms
        self.namespace = namespace
        self.uname_sid_map = {}
        room_ids = [str(uuid1(i)) for i in range(num_rooms)]
        self.room_members = {uid: set() for uid in room_ids}
        self.room_counts = {key: 0 for key in room_ids}

    def add_user(self,username, request, room_id=None):
        room_id = room_id
        self.uname_sid_map[username] = request.sid
        if room_id is None:
            keys_list = list(self.room_members.keys())
            idx = random.randint(0,self.num_rooms-1)
            room_id = keys_list[idx]

        self.room_members[room_id].add(username)
        join_room(room_id,request.sid,request.namespace)
        return room_id
    
    def get_room_count(self, room_id):
        return self.room_counts[room_id]
    
    def increment_room_count(self,room_id):
        if room_id in self.room_counts:
            self.room_counts[room_id] += 1
            return self.room_counts[room_id]
        else:
            print("YPPPPPP")
        