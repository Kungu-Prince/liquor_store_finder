from flask import render_template, request, jsonify
from app import app, db
from app.models import Store
from app.utils import haversine

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stores')
def stores():
    user_lat = float(request.args.get('lat', 1.2921))  # Default to Nairobi's coordinates
    user_lon = float(request.args.get('lon', 36.8219))
    stores = Store.query.all()

    # Calculate distance and filter stores
    store_data = []
    for store in stores:
        distance = haversine(user_lat, user_lon, store.latitude, store.longitude)
        if distance <= 10:  # Example filter for 10 km
            store_data.append({
                'id': store.id,
                'name': store.name,
                'description': store.description,
                'image_url': store.image_url,
                'opening_time': store.opening_time.strftime('%H:%M'),
                'distance': round(distance, 2)
            })

    store_data = sorted(store_data, key=lambda x: x['distance'])  # Sort by distance

    return jsonify({'stores': store_data})
