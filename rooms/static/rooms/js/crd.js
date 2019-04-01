function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

Rooms = new Vue({
    el: '#rooms',
    delimiters: ['${','}'],
    data: {
       rooms: [],
       loading: false,
       csrftoken:getCookie('csrftoken'),
       newRoom: { 
        'name': null,
        "combo":null, 
        'deck': null,
        'number_of_players':null, 
        },
       currentRoom: {},

    },
    http:{
        root: 'http://localhost:8000',
        headers: {
          "Access-Control-Allow-Origin": '*',
          "X-CSRFToken": getCookie('csrftoken'),
          "Accept": "application/json"
        }
    },
    mounted: function() {
        this.getRooms();
    },
    methods: {
        getRooms: function() {
          this.loading = true;
          this.$http.get('/api/room/')
              .then((response) => {
                this.rooms = response.data;
                this.loading = false;
              })
              .catch((err) => {
               this.loading = false;
               console.log(err);
              })
         },
        getRoom: function(id) {
          this.loading = true;
          this.$http.get('/api/room/'+id+'/')
              .then((response) => {
                this.currentRoom = response.data;
                $("#detailModal").modal('show');
                this.loading = false;
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
              })
         },
        addRoom: function() {
          this.loading = true;
          this.$http.post('/api/room/create-room/',this.newRoom)
              .then((response) => {
                this.loading = false;
                $("#addRoomModal").modal('hide');
                this.getRooms();
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
              })
         },
        deleteRoom: function(id) {
          this.loading = true;
          this.$http.delete('/api/room/'+id+'/' )
              .then((response) => {
                this.loading = false;
                this.getRooms();
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
              })
        }
    }
});