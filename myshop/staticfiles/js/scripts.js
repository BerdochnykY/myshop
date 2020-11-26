$(document).ready(function(){
  var form = $('#form_buying_product');
  console.log(form);
  form.on('submit', function(e){
    e.preventDefault();
    console.log('123');
    var nmb = $('#number').val();
    console.log(nmb);
    var submit_btn = $('#submit_btn');
    var product_id = submit_btn.data("product_id");
    var product_name = submit_btn.data("name");
    var product_price = submit_btn.data("price");
    console.log(product_id);
    console.log(product_name);

    var data = {};
    data.product_id = product_id;
    data.nmb = nmb;
     var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
     data["csrfmiddlewaretoken"] = csrf_token;

     var url = form.attr("action");

console.log(data)

     $.ajax({
       url: url,
       type: 'POST',
       data: data,
       cache: true,
       success: function (data) {
         console.log("OK");
         console.log(data.products_total_nmb)
         if (data.products_total_nmb) {
           $('#basket_total_nmb').text("("+data.products_total_nmb+")");
         }

       },
       error: function() {
         console.log("errorr");
       },
     });
console.log(url)

    $('.basket-items ul').append('<li>'+product_name+', ' + nmb + 'шт. ' + 'по ' + product_price + 'грн  ' +
      '<a class="delete-item" href="">x</span>'+
      '</li>');

  });

//Отображение и скрытие корзины
  $('.basket-container').hover(function() {
    $('.basket-items').show();
  },
  function() {
    $('.basket-items').hide();
    });

  $(document).on('click', '.delete-item', function(){
    $(this).closest('li').remove()
  })

});
