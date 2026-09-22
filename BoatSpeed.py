def boat(boat_speed,stream_speed,distance,stream_direction):
    if stream_direction == "up":
        speed = boat_speed-stream_speed
        time = distance/speed
    elif stream_direction == "down":
        speed = boat_speed+stream_speed
        time = distance/speed
    else:
        print("no")
    return time
