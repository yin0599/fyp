var express = require('express'); 
var app = express();

var mysql = require("mysql");
var bodyParser = require('body-parser');

app.use(bodyParser.json({type:'application/json'}));
app.use(bodyParser.urlencoded({extends:true}));

var con = mysql.createConnection({ //sql connection

    host:'localhost',
    port:'3306',
    user:'root',
    password:'123456',
    database:'example'

});

var server = app.listen(4545, function(){ //cearte port link address
    var host =server.address().address
    var port =server.address().port
    console.log("start");
});


con.connect(function(error){ // error checking for connection 
    if(error)
    console.log(error);
    else console.log("connected");
});

app.get('/send_data', function(req, res){ //get data to a singal path
    con.query('select * from send_data' , function(error, rows ,fields){
       if(error) console.log(error);
       
       else{
        console.log(rows);
        res.send(rows);
       }
    });
});
// module.exports = app;