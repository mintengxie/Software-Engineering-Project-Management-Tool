function createteam(){
$("#myModal").modal('show');
}

//toggle the search bar
function search_show(){

  // search bar is hidden
  if ($('div#message_search').attr('class').indexOf('hidden') == -1) {
    $('div#message_search').addClass('hidden');
    $('div.messagecontent').css('padding-top', '70px');
  } 
  else {
    $('div#message_search').removeClass('hidden');
    $('div.messagecontent').css('padding-top', '130px');
  }
}

// global state variables
global_room_list = [];
global_user_list = [];

var server_host = window.location.hostname;
var base_url = 'http://' + server_host + ':3000/';
var global = io('http://' + server_host + ':3000');

console.log('username: ' + user);

global.emit('user', {
  'username': user,
  'action': 'connect',
});
global.on('user', function(user){

  var user_link = $('ul.user_list a').filter( function(link) { return $(this).text() === user.username }).parent();

  if (user.action == 'connected') {
    user_link.removeClass('disabled');
  } else if (user.action == 'disconnected') {
    user_link.addClass('disabled');
  }
  
});

sockets = {};
$.getJSON('http://' + server_host + '/api/rooms/',function(data){
  data.forEach(function(room){
    var socket = io(base_url + room.id);
    socket.on('msg', function(msg) {
      if (room.id != visible_namespace()) {
        increment_badge(room.id);
      }
      add_message('<b>' + msg.username + '</b>: ' + msg.value, room.id); 
    });
    sockets[room.id] = socket;
  });
});


function increment_badge(room_id){
  var badge = $('div#room-list a').filter( function(){ return $(this).attr('id') === 'room-' + room_id } ).children().filter('.badge');
  var count = Number(badge.text());
  badge.text(count += 1);
}

function add_message(msg, target) {
  $('div#room-' + target).append(msg + '<br>');
}

function visible_namespace() {
  try {
    return Number($('div.messagecontent').filter(':visible').attr('id').replace('room-',''));
  } catch (TypeError) {
    return null;
  }
}

// function create_team(){
//   $('#add_team_modal').modal('show');
// }

// Called when button is clicked
function display() {
  console.log('sending message...');
  var message = {
    'username': user,
    'value': $('input#text').val(),
    'user_id': user_id
  }
  sockets[visible_namespace()].emit('msg', message);
  $('input#text').val('');
}

// Generate random user
function random_user() {
  var random_index = Math.floor( Math.random() * 100 ) + 1;
  return "User " + random_index;
}

// Add a new message whenever the user presses the enter key
$(document).keypress(function(e) {
    if(e.which == 13) {
        display();
    }
});


var mobile_nav = {
  'message': function() {
    $('div.sidebar').addClass('hidden-xs hidden-sm');
    $('div.message').removeClass('hidden-xs hidden-sm');
  },
  'sidebar': function() {
    $('div.message').addClass('hidden-xs hidden-sm');
    $('div.sidebar').removeClass('hidden-xs hidden-sm');
  }
}


function switch_room(target_room){

  // Mobile navigation
  mobile_nav.message();

  var room_id = Number(target_room.replace('room-',''));
  var room_name = _.filter(global_room_list, function(obj){ return (obj.id === room_id) })[0].name;

  $('span#room_title').text(room_name);

  global_room_list.forEach( function(room){

    var room_num = 'room-' + room.id;
    if (room_num === target_room) {
      $('div.messagecontent').filter('#' + room_num).show();
      $('div#room-list a').filter('#' + room_num).attr('class', 'list-group-item room-link active');
    } else {
      $('div.messagecontent').filter('#' + room_num).hide();
      $('div#room-list a').filter('#' + room_num).attr('class', 'list-group-item room-link');
    }

  });

  // reset the badge count for the target room
  $('div#room-list a').filter( function(){ return $(this).attr('id') === target_room } ).children().filter('.badge').text('');

}

function get_message_data(room_id) {

    var message_endpoint = 'http://' + server_host + '/api/messages/?format=json';
    $.getJSON(message_endpoint, function(data){
      data.forEach(function(msg){
        message_room = Number(msg.room.split('/api/rooms/')[1].slice(0,-1));
        if (message_room === room_id) { add_message(msg.text, room_id) };
      });
    });

}


function populate_room_list() {

  $.getJSON('http://' + server_host + '/api/rooms/?format=json', function(data) { 
    global_room_list = data;
    data.forEach(function(room) {

      var room_link = $('<a />', {
        'href': '#',
        'id': 'room-' + room.id,
        'class': 'list-group-item room-link'
      })
      .append( $('<span />', {
        'class': 'glyphicon glyphicon-comment padded-icon',
        'ariad-hidden': true
      }))
      .append(room.name)
      .append( $('<span />',{
        'class': 'badge'
      }));

      $('div#room-list').append(room_link)

      // add room to message list
      $('div#message_list').append( $('<div />', {
        'class': 'messagecontent',
        'id': 'room-' + room.id,
        'text': '',
      }));

      get_message_data(room.id);

    });

    switch_room('room-' + global_room_list[0].id);

  });
}

function populate_user_list() {
  $.getJSON('http://' + server_host + '/api/users/?format=json', function(all_users) { 

    $.getJSON('http://' + server_host + ':3000/users', function(connected_users){

      // make sure the current user is included in the list
      connected_users.push(user);
      online_users = _.unique(connected_users);

      global_user_list = all_users;
      all_users.forEach(function(user) {
        var user_link = $('<li />', {
          'class': _.contains(online_users, user.username) ? 'user' : 'user disabled',
          'html': 
          $('<a />', {
            'href': '#'
          })
          .append( $('<span />', {
            'class': 'glyphicon glyphicon-user padded-icon'
            })).append(user.username)
        })

        $('ul.user_list').append(user_link);

      });
    });
  });
}
//upload file
function filechoose(){
$("#inputmodal").modal('show');
}
$(document).on('change', '.btn-file :file', function() {
  var input = $(this),
      numFiles = input.get(0).files ? input.get(0).files.length : 1,
      label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
  input.trigger('fileselect', [numFiles, label]);
});
$(document).ready( function() {
    $('.btn-file :file').on('fileselect', function(event, numFiles, label) {
        
        var input = $(this).parents('.input-group').find(':text'),
            log = numFiles > 1 ? numFiles + ' files selected' : label;
        
        if( input.length ) {
            input.val(log);
        } else {
            if( log ) alert(log);
        }
        
    });
});

// MAIN
$(document).ready(function(){

  populate_room_list();
  populate_user_list();

  $('div#room-list').on('click', 'a', function(){ 
    if ($(this).attr('id') != 'create-room' ) {
      switch_room( $(this).attr('id') );
    }
  });

  mobile_nav.sidebar();

  $('form#file_upload').submit(function(event){
    $.ajax({
      url: 'http://' + server_host + ':3000/upload',
      type: 'POST',
      data: new FormData( this ), 
      processData: false,
      contentType: false,
      success: function(file_path){ 
        var download_url = 'http://' + server_host + '/' + file_path;
        var display_name = $('input#filename').val();
        $('input#text').val('<a href="' + download_url + '">' + display_name + '</a>' );
        display();
        $('#inputmodal').modal('hide');
      }
    });
    event.preventDefault();
  });

});

    



