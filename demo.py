from exif import Image

def get_image_info(image_path):
    try:
        # Open the image file in binary read mode
        with open(image_path, 'rb') as image_file:
            my_image = Image(image_file)

        # Check if the image actually has EXIF data
        if not my_image.has_exif:
            print("This image does not contain EXIF data.")
            return

        # 1. Get Date and Time
        datetime = my_image.get('datetime_original', 'Unknown Time')
        print(f"Time Taken: {datetime}")

        # 2. Get Location (if available)
        if hasattr(my_image, 'gps_latitude') and hasattr(my_image, 'gps_longitude'):
            # Grab the raw coordinates and reference directions (N/S, E/W)
            lat = my_image.gps_latitude
            lat_ref = my_image.gps_latitude_ref
            lon = my_image.gps_longitude
            lon_ref = my_image.gps_longitude_ref

            print(f"Raw Latitude: {lat} {lat_ref}")
            print(f"Raw Longitude: {lon} {lon_ref}")

            # Convert the raw coordinates into decimal format for Google Maps
            decimal_lat = lat[0] + (lat[1] / 60) + (lat[2] / 3600)
            if lat_ref == 'S': 
                decimal_lat = -decimal_lat
            
            decimal_lon = lon[0] + (lon[1] / 60) + (lon[2] / 3600)
            if lon_ref == 'W': 
                decimal_lon = -decimal_lon

            print(f"Google Maps Link: https://www.google.com/maps?q={decimal_lat},{decimal_lon}")
        else:
            print("No GPS location data found in this image.")
            
    except FileNotFoundError:
        print(f"Error: Could not find '{image_path}'. Check that the image is in the same folder as this script!")

# Run the function on our image
get_image_info('photo.jpg')