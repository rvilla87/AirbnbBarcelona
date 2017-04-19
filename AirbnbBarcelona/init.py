import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gmaps
import sys
import secret

# Leemos los ficheros

"""
- listings.csv (17672 líneas)	Summary information and metrics for listings in Barcelona (good for visualisations).

id,name,host_id,host_name,neighbourhood_group,neighbourhood,latitude,longitude,room_type,price,minimum_nights,number_of_reviews,last_review,reviews_per_month,calculated_host_listings_count,availability_365

8207551,Room in Sant Antoni huge terrasse,7783989,Christophe,Ciutat Vella,el Raval,41.3808442104594,2.1638396776108855,Private room,39,1,2,2015-09-27,0.11,2,0

"""
listing = pd.read_csv('datasets/listings.csv')
lista=listing.head(4).values[:,6:8].tolist()
print("listing normal:")
print(lista)

"""
- listings.csv.gz (50853 líneas)	Detailed Listings data for Barcelona

id,listing_url,scrape_id,last_scraped,name,summary,space,description,experiences_offered,neighborhood_overview,notes,transit,access,interaction,house_rules,thumbnail_url,medium_url,picture_url,xl_picture_url,host_id,host_url,host_name,host_since,host_location,host_about,host_response_time,host_response_rate,host_acceptance_rate,host_is_superhost,host_thumbnail_url,host_picture_url,host_neighbourhood,host_listings_count,host_total_listings_count,host_verifications,host_has_profile_pic,host_identity_verified,street,neighbourhood,neighbourhood_cleansed,neighbourhood_group_cleansed,city,state,zipcode,market,smart_location,country_code,country,latitude,longitude,is_location_exact,property_type,room_type,accommodates,bathrooms,bedrooms,beds,bed_type,amenities,square_feet,price,weekly_price,monthly_price,security_deposit,cleaning_fee,guests_included,extra_people,minimum_nights,maximum_nights,calendar_updated,has_availability,availability_30,availability_60,availability_90,availability_365,calendar_last_scraped,number_of_reviews,first_review,last_review,review_scores_rating,review_scores_accuracy,review_scores_cleanliness,review_scores_checkin,review_scores_communication,review_scores_location,review_scores_value,requires_license,license,jurisdiction_names,instant_bookable,cancellation_policy,require_guest_profile_picture,require_guest_phone_verification,calculated_host_listings_count,reviews_per_month

8207551,https://www.airbnb.com/rooms/8207551,20170407214050,2017-04-08,Room in Sant Antoni huge terrasse,"Located between Sant Antoni & Universitat (metro L2 & L1). We are renting 1 large double bedroom + 1 bathroom.  Located at the 7th floor and offer a huge terrace with an amazing view.  The apartment is very clean, new and full equipped.","the apartment is located on the 7th floor and has an 80sqm terrace overlooking the city. It is definitely the perfect place to relax after a full day of sight seeing. there are windows and balconies all around the flat making it very light and breezy, the living room, dining room, and kitchen have all the amenities you may need. It was just recently renovated so rest assured everything is new. It is a 100sqm 4 bedroom flat, with 2 bathrooms. With AC and heating system which will make your stay truly comfortable.","Located between Sant Antoni & Universitat (metro L2 & L1). We are renting 1 large double bedroom + 1 bathroom.  Located at the 7th floor and offer a huge terrace with an amazing view.  The apartment is very clean, new and full equipped. the apartment is located on the 7th floor and has an 80sqm terrace overlooking the city. It is definitely the perfect place to relax after a full day of sight seeing. there are windows and balconies all around the flat making it very light and breezy, the living room, dining room, and kitchen have all the amenities you may need. It was just recently renovated so rest assured everything is new. It is a 100sqm 4 bedroom flat, with 2 bathrooms. With AC and heating system which will make your stay truly comfortable. You can access all common spaces including living, dining room, kitchen and terrace It's a very friendly flat, we are all friends from our masters program and work. We speak in english, portuguese, french, japanese and spanish. We will take time",none,"Sant Antoni is a very central neighborhood and not too touristy which makes it very relaxing at the same time. It is part of the eixample neighborhood, bordering raval and universitat. Very central since the gothic area is just behind. The Sant Antoni market is just in front of the doorstep","","Sant antoni metro (purple line L1) and universitat metro (red line L2), the aerobus from the airport drops you in universitat and its a 5 min walk from the flat, cabs and bus stops all around the area","You can access all common spaces including living, dining room, kitchen and terrace","It's a very friendly flat, we are all friends from our masters program and work. We speak in english, portuguese, french, japanese and spanish. We will take time to assist you in any query you have","",https://a0.muscache.com/im/pictures/104461840/f67039f8_original.jpg?aki_policy=small,https://a0.muscache.com/im/pictures/104461840/f67039f8_original.jpg?aki_policy=medium,https://a0.muscache.com/im/pictures/104461840/f67039f8_original.jpg?aki_policy=large,https://a0.muscache.com/im/pictures/104461840/f67039f8_original.jpg?aki_policy=x_large,7783989,https://www.airbnb.com/users/show/7783989,Christophe,2013-07-28,"Barcelona, Catalonia, Spain",Je parle Français et anglais,N/A,N/A,N/A,f,https://a0.muscache.com/im/users/7783989/profile_pic/1379453966/original.jpg?aki_policy=profile_small,https://a0.muscache.com/im/users/7783989/profile_pic/1379453966/original.jpg?aki_policy=profile_x_medium,El Raval,2,2,"['email', 'phone', 'reviews', 'jumio']",t,t,"El Raval, Barcelona, Catalunya 08001, Spain",El Raval,el Raval,Ciutat Vella,Barcelona,Catalunya,08001,Barcelona,"Barcelona, Spain",ES,Spain,41.3808442104594,2.1638396776108855,t,Apartment,Private room,2,1.0,1,1,Real Bed,"{TV,Internet,""Wireless Internet"",""Air conditioning"",Kitchen,""Elevator in building"",""Buzzer/wireless intercom"",Heating,Washer,Essentials,Shampoo}",,$39.00,,,,$15.00,1,$0.00,1,1125,18 months ago,,0,0,0,0,2017-04-08,2,2015-09-25,2015-09-27,100,9,10,10,10,10,10,t,,,f,strict,f,f,2,0.11
"""
listing_detail = pd.read_csv('datasets/listings.csv.gz')
lista_detail = listing_detail.head(1).drop(['summary', 'space', 'description', 'neighborhood_overview', 'transit' , 'access', 'interaction'], axis=1)
lista_detail.to_excel("lista_detail.xls")

# Pendiente hacer:
# 1- Identificar los campos del excel generado que me pueden interesar (id, imagenes?, precio, nombre, coordenadas, tipo de propiedad, habitaciones, baños, licencia?, ultima vez que actualizo calendario, valoraciones/valoraciones por mes? )
# 2- Filtrar por precio, disponibilidad, etc.
# 3- Ordenar por precio, calendario actualizado, etc.
# 3- Mostrar algo de lo identificado en el gmaps (al ponerse sobre el punto que muestre una imagen?)


"""
- calendar.csv.gz	Detailed Calendar Data for listings in Barcelona

listing_id,date,available,price

8207551,2018-04-06,f,
13069815,2017-06-11,t,$40.00
"""





# Estos ficheros en principio no los voy a usar
"""
- reviews.csv	Summary Review data and Listing ID (to facilitate time based analytics and visualisations linked to a listing).
- reviews.csv.gz	Detailed Review Data for listings in Barcelona
- neighbourhoods.csv	Neighbourhood list for geo filter. Sourced from city or open source GIS files.
- neighbourhoods.geojson	GeoJSON file of neighbourhoods of the city.
"""

