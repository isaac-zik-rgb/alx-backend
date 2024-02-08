import { createClient } from "redis";
import { Express } from "express";
import { promisify } from "util";

//create express server app
const app = Express();

//create redis client
const client = createClient();

client.on('connect', function() {
    console.log('Redis client connected to the server');
});

client.on('error', function (err) {
    console.log(`Redis client not connected to the server: ${err}`);
});

//promisify client.get function
const get = promisify(client.get).bind(client);

const listProducts = [
    { 'itemId': 1, 'itemName': 'Suitcase 250', 'price': 50, 'initialAvailableQuantity': 4},
  { 'itemId': 2, 'itemName': 'Suitcase 450', 'price': 100, 'initialAvailableQuantity': 10},
  { 'itemId': 3, 'itemName': 'Suitcase 650', 'price': 350, 'initialAvailableQuantity': 2},
  { 'itemId': 4, 'itemName': 'Suitcase 1050', 'price': 550, 'initialAvailableQuantity': 5}
];

// retrive item by id
function getItemById(itemId) {
    return listProducts.filter((item) => item.itemId === itemId)[0];
}

function reserverStockById(itemId, stock) {
    client.set(itemId, stock);
}

//express routes
app.get('/list_products', (req, res) => {
    res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const item = getItemById(itemId);
    res.json(item);
});

if (item) {
    const stock = await getCurrentReservedStockById(itemId);
    const resItem = {
      itemId: item.itemId,
      itemName: item.itemName,
      price: item.price,
      initialAvailableQuantity: item.initialAvailableQuantity,
      currentQuantity: stock !== null ? parseInt(stock) : item.initialAvailableQuantity,
    };
    res.json(resItem);
  } else {
    res.json({"status": "Product not found"});
  }
});

app.get('/reserve_product/:itemId', async function (req, res) {
  const itemId = req.params.itemId;
  const item = getItemById(parseInt(itemId));

  if (!item) {
    res.json({"status": "Product not found"});
    return;
  }

  let currentStock = await getCurrentReservedStockById(itemId);
  if (currentStock !== null) {
    currentStock = parseInt(currentStock);
    if (currentStock > 0) {
      reserveStockById(itemId, currentStock - 1);
      res.json({"status": "Reservation confirmed", "itemId": itemId});
    } else {
      res.json({"status": "Not enough stock available", "itemId": itemId});
    }
  } else {
    reserveStockById(itemId, item.initialAvailableQuantity - 1);
    res.json({"status": "Reservation confirmed", "itemId": itemId});
  }
});


//set up express server
const port = 1245;
app.listen(port, () => {
  console.log(`app listening at http://localhost:${port}`);
});
