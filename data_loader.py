import overpy

api = overpy.Overpass()

result = api.query("""<osm-script>
  <query type="node">
    <has-kv k="place" v="city"/>
    <bbox-query e="8" n="51" s="42" w="-5"/>   
  </query>
  <print/>
</osm-script>""")
