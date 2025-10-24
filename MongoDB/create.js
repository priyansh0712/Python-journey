try {
   db.products.insertOne( { item: "card", qty: 15 } );
} catch (e) {
   print (e);
};