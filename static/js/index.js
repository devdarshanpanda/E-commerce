
let cart_plus=document.getElementById("cart_plus")
let cart_minus=document.getElementById("cart_minus")
let cart_quantity=document.getElementById("cart_quantity")
let cart_quantity_value=parseInt(cart_quantity.value)
// console.log(typeof(cart_quantity_value));
// let counter=0
cart_plus.addEventListener("click",()=>{
    // console.log(cart_quantity_value);
    cart_quantity.value=cart_quantity_value+=1
    // console.log(cart_quantity+=1);
    // counter++;
    // cart_quantity.value=counter;
    // console.log(counter);
    
})



cart_minus.addEventListener("click",()=>{
    // cart_quantity.value=cart_quantity_value-1
    if(cart_quantity_value >=1){
        cart_quantity.value=cart_quantity_value-=1
    }
   
})


document.getElementById('contact-link').addEventListener('click', function(e) {
    e.preventDefault();
    document.getElementById('contact').scrollIntoView({ behavior: 'smooth' });
});






// <section>
// <div class="container">
//   <div class=" mt-4">
//     <h3 class="text-center">Check our <span class="text-danger">Product</span></h3>
//   </div>
//     {% comment %} -----------------------------top were start------------------------------  {% endcomment %}

//   <div class="row mt-5">
//     <div class=" mt-4">
//       <h3 class="text-danger text-center py-3"  style=" border-bottom: 1px solid red; border-top: 1px solid red;">Top Were</h3>
//     </div>
//     {% for i in top_were %}
//     <div class="col-md-3 d-flex justify-content-center">
     
//       <div class="card mt-4 mb-2" style="width: 18rem; height:25em">
//         <div class="" style="height:50%; width:100%;">

//           <img class="img-fluid img" src="media/{{i.img}}" alt="Card image cap" style="height: 100%; width: 100%;">
//         </div>

//         <div class="card-body">
//           <h4 class="card-text">{{i.brand}}</h4>
//           <p class="card-text text-danger">Price:{{i.selling_price}}</p>
//           <p class="card-text">Discounted price: {{i.discounted_price}}</p>
//           <button type="button" class="btn btn-danger">Add to cart</button>

//         </div>
//       </div>
//       {% if forloop.counter|divisibleby:4 and not forloop.last %}
//       </div><div class="row">
//         {% endif %}
//       </div>
//       {% endfor %}
//       </div>

//   </div>
// {% comment %} -----------------------------top were end------------------------------  {% endcomment %}
// {% comment %} -----------------------------bottom were start------------------------------  {% endcomment %}
// <div class="row mt-5">
//   <div class=" mt-4">
//     <h3 class="text-danger text-center py-3"  style=" border-bottom: 1px solid red; border-top: 1px solid red;">Bottom Were</h3>
//   </div>
//   {% for i in bottom_were %}
//   <div class="col-md-3 d-flex justify-content-center">
   
//     <div class="card mt-4 mb-2" style="width: 18rem; height:25em">
//       <div class="" style="height:50%; width:100%;">

//         <img class="img-fluid img" src="media/{{i.img}}" alt="Card image cap" style="height: 100%; width: 100%;">
//       </div>

//       <div class="card-body">
//         <h4 class="card-text">{{i.brand}}</h4>
//         <p class="card-text text-danger">Price:{{i.selling_price}}</p>
//         <p class="card-text">Discounted price: {{i.discounted_price}}</p>
//         <button type="button" class="btn btn-danger">Add to cart</button>

//       </div>
//     </div>
//     {% if forloop.counter|divisibleby:4 and not forloop.last %}
//     </div><div class="row">
//       {% endif %}
//     </div>
//     {% endfor %}
//     </div>

// </div>
// {% comment %} -----------------------------bottom were end------------------------------  {% endcomment %}
// {% comment %} -----------------------------mobile start------------------------------  {% endcomment %}
// <div class="row mt-5">
//   <div class=" mt-4">
//     <h3 class="text-danger text-center py-3"  style=" border-bottom: 1px solid red; border-top: 1px solid red;">Mobile</h3>
//   </div>
//   {% for i in mobile %}
//   <div class="col-md-3 d-flex justify-content-center">
   
//     <div class="card mt-4 mb-2" style="width: 18rem; height:25em">
//       <div class="" style="height:50%; width:100%;">

//         <img class="img-fluid img" src="media/{{i.img}}" alt="Card image cap" style="height: 100%; width: 100%;">
//       </div>

//       <div class="card-body">
//         <h4 class="card-text">{{i.brand}}</h4>
//         <p class="card-text text-danger">Price:{{i.selling_price}}</p>
//         <p class="card-text">Discounted price: {{i.discounted_price}}</p>
//         <button type="button" class="btn btn-danger">Add to cart</button>

//       </div>
//     </div>
//     {% if forloop.counter|divisibleby:4 and not forloop.last %}
//     </div><div class="row">
//       {% endif %}
//     </div>
//     {% endfor %}
//     </div>

// </div>
// {% comment %} -----------------------------mobile end------------------------------  {% endcomment %}
// {% comment %} -----------------------------laptop start------------------------------  {% endcomment %}
// <div class="row mt-5">
//   <div class=" mt-4">
//     <h3 class="text-danger text-center py-3"  style=" border-bottom: 1px solid red; border-top: 1px solid red;">Laptop</h3>
//   </div>
//   {% for i in laptop %}
//   <div class="col-md-3 d-flex justify-content-center">
   
//     <div class="card mt-4 mb-2" style="width: 18rem; height:25em">
//       <div class="" style="height:50%; width:100%;">

//         <img class="img-fluid img" src="media/{{i.img}}" alt="Card image cap" style="height: 100%; width: 100%;">
//       </div>

//       <div class="card-body">
//         <h4 class="card-text">{{i.brand}}</h4>
//         <p class="card-text text-danger">Price:{{i.selling_price}}</p>
//         <p class="card-text">Discounted price: {{i.discounted_price}}</p>
//         <button type="button" class="btn btn-danger">Add to cart</button>

//       </div>
//     </div>
//     {% if forloop.counter|divisibleby:4 and not forloop.last %}
//     </div><div class="row">
//       {% endif %}
//     </div>
//     {% endfor %}
//     </div>

// </div>
// {% comment %} -----------------------------laptop end------------------------------  {% endcomment %}


  

// </div>
// </section>