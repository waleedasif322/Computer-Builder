$(function() {


    var cpu_list = [
    "cpu 1",
    "cpu 2",
    "cpu 3",
    "cpu 4",
    "cpu 5",
    "cpu 6", 
    "cpu 7",
    "cpu 8",
    "cpu 9"
    ];


   //var cpu_list = []
   //{% for item in cpus %}
   //  cpu_list.push("{{item}}")
   //{% endfor %}
   //for(var i=0; i <cpu_list.length;i++)
   //   {alert(cpu_list[i])}

    $("#cpu_input").autocomplete({
        minLength: 2,
        source: cpu_list
    });

    /*
    //Get autocomplete results from server
    //with local caching

    var products_page = "get_products";

    // cpu autocomplete

    var cpu_cache = {};
    $("#cpu_input).autocomplete({
        minLength: 2,
        source: function(request, response) {
            var term = request.term;
            if (term in cpu_cache) {
                response(cpu_cache[term]);
                return;
            }

            $.getJSON(products_page, request, function(data, status, xhr) {
                cpu_cache[term] = data;
                response(data);
            });
        }
    });

    // motherboard autocomplete

    var mobo_cache = {};
    $("#mobo_input).autocomplete({
        minLength: 2,
        source: function(request, response) {
            var term = request.term;
            if (term in mobo_cache) {
                response(mobo_cache[term]);
                return;
            }

            $.getJSON(products_page, request, function(data, status, xhr) {
                mobo_cache[term] = data;
                response(data);
            });
        }
    });

    // memory autocomplete
    
    var mem_cache = {};
    $("#mem_input).autocomplete({
        minLength: 2,
        source: function(request, response) {
            var term = request.term;
            if (term in mem_cache) {
                response(mem_cache[term]);
                return;
            }

            $.getJSON(products_page, request, function(data, status, xhr) {
                mem_cache[term] = data;
                response(data);
            });
        }
    });

    // video card autocomplete
    
    var gpu_cache = {};
    $("#gpu_input).autocomplete({
        minLength: 2,
        source: function(request, response) {
            var term = request.term;
            if (term in gpu_cache) {
                response(gpu_cache[term]);
                return;
            }

            $.getJSON(products_page, request, function(data, status, xhr) {
                gpu_cache[term] = data;
                response(data);
            });
        }
    });

    // hard drive autocomplete
    
    var hdd_cache = {};
    $("#hdd_input).autocomplete({
        minLength: 2,
        source: function(request, response) {
            var term = request.term;
            if (term in hdd_cache) {
                response(hdd_cache[term]);
                return;
            }

            $.getJSON(products_page, request, function(data, status, xhr) {
                hdd_cache[term] = data;
                response(data);
            });
        }
    });

    // case autocomplete

    var hdd_cache = {};
    $("#hdd_input).autocomplete({
        minLength: 2,
        source: function(request, response) {
            var term = request.term;
            if (term in hdd_cache) {
                response(hdd_cache[term]);
                return;
            }

            $.getJSON(products_page, request, function(data, status, xhr) {
                hdd_cache[term] = data;
                response(data);
            });
        }
    });


*/

    
});
