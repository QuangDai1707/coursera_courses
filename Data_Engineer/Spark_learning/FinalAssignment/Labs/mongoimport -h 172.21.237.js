mongoimport -h 172.21.237.158:27017 -u root -p vkyDebgE0f014yseTdykeWYL --authenticationDatabase admin --db catalog --collection electronics --file catalog.json
mongoexport -h 172.21.237.158:27017 -u root -p vkyDebgE0f014yseTdykeWYL --authenticationDatabase admin --db catalog --collection electronics --out electronics.csv --type=csv --fields _id,type,model



db.electronics.aggregate([{ $match: { type: "smart phone" } }, 
  { 
    $group: { 
      _id: "$type", 
      averageScreenSize: { $avg: "$screen size" } 
        } 
  }
]);


