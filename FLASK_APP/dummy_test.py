import json as js
import pickle


class JsonPickle:
    def create_pickle(self):
        with open('dummy.json', 'r') as f:
            dummy = js.load(f)
        outfile = open('example', 'wb')
        pickle.dump(dummy, outfile)
        outfile.close()

    def __repr__():
        print(outfile)

a = JsonPickle()

a.create_pickle()

print(a.create_pickle())

# print(dummy['username'])
#
# for i in dummy:
#     newDummy = dummy[i]
#     print(dummy[i])
#
# print("done")


# @APP.route('/api/', methods=['POST']
# def request_info():
#     response = request.post(json='dummy.json')
#     data = request.get_json()
#     return data
#
# print(request_info())

# accomodates = [1, 2, 3, 4, 5, 6, 7, 8]
# bathrooms = dummy['bathrooms']
# bedrooms = dummy['bedrooms']
# beds = dummy['beds']
#
# bed_type = [Real Bed, Pull-out Sofa, Futon, Couch, Airbed]
# instant_bookable = [0, 1] <---boolean
# minimum_nights = [1, 2, 3, 4, 5, 6, 7]
# neighborhood = [Friedrichshain-Kreuzberg, Mitte, Pankow, Neukolln]
# room_type = [Private room, Entire home/apt, Shared room]
# wifi = [0, 1]  <---boolean

