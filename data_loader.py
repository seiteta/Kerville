import OsmApi
MyApi = OsmApi.OsmApi()

for i in range(26686348,26686552):
    node = MyApi.NodeGet(i)
    if node is not None:
        if 'tag' in node.keys():     
            if 'place' in node['tag']:
                place_type = node['tag']['place']
                if place_type == 'city' or place_type == 'town' or place_type == 'village':
                    print node['tag']['name']
