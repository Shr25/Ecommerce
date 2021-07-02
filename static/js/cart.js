if (localStorage.getItem("cart") == null) {
  var cart = {};
} else {
  cart = JSON.parse(localStorage.getItem("cart"));
  updateCart(cart);
}

//  add/increment the item
$(".divpr").on("click", "button.cart", function () {
  var idstr = this.id.toString();
  if (cart[idstr] != undefined) {
    qty = cart[idstr][0] + 1;
  } else {
    qty = 1;
    productName = document.getElementById("name" + idstr).innerHTML;
    price = document.getElementById("price" + idstr).innerHTML;
    cart[idstr] = [qty, productName, parseInt(price)];
  }
  updateCart(cart);
});

function clearCart() {
  cart = JSON.parse(localStorage.getItem("cart"));
  for (let item in cart) {
    document.getElementById("div" + item).innerHTML =
      '<button id="' +
      item +
      '" class="btn cart-btn-1 text-white cart"> Add To Cart</button>';
  }
  localStorage.clear();
  cart = {};
  updateCart(cart);
}

function updateCart(cart) {
  let sum = 0;
  for (let item in cart) {
    sum = sum + cart[item][0];
    document.getElementById("div" + item).innerHTML ="<button id='minus" +
    item +
    "' class='btn cart-btn-1 text-white minus'>-</button> <span id='val" +
    item +
    "''>" +
    cart[item][0] +
    "</span> <button id='plus" +
    item +
    "' class='btn cart-btn-1 text-white plus'> + </button>";
      
  }
  localStorage.setItem("cart", JSON.stringify(cart));
  document.getElementById("cart").innerHTML = sum;
  // console.log(cart);
}

//  change the cart as well as the display value
$(".divpr").on("click", "button.minus", function () {
  a = this.id.slice(7, );
  cart["pr" + a][0] = cart["pr" + a][0] - 1;
  cart["pr" + a][0] = Math.max(0, cart["pr" + a][0]);
  document.getElementById("divpr" + a).innerHTML = '<button id="pr{{i.id}}" class="btn cart-btn-1 text-white cart">Add To Cart</button>';
  updateCart(cart);
});
$(".divpr").on("click", "button.plus", function () {
  a = this.id.slice(6, );
  cart["pr" + a][0] = cart["pr" + a][0] + 1;
  document.getElementById("valpr" + a).innerHTML = cart["pr" + a][0];
  updateCart(cart);
});
