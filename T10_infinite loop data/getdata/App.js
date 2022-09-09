import React, {Component} from 'react';
import {Platform, StyleSheet, Text, View,FlatList, Button} from 'react-native';

export default class App extends React.Component {
  constructor(props){
    super(props);
    this.state ={data:[]};
  }

  fetchData = async()=>{
    const response = await fetch('http://172.28.234.169:4545/send_data');// grap data
    const users = await response.json();
    this.setState({data: users});
  }


  componentDidMount(){ //reflash and get new data
    this.dataID = setInterval(
      () => this.fetchData(),1000
    );
  }
  
  componentWillUnmount(){ // clean old data 
    clearInterval(this.data);
  }

  render() {// layout 
    return (
      <View >
        <Text>Welcome</Text>

        <Button title='click' onPress={() =>{ this.componentDidMount()}}/>

        <FlatList
        data={this.state.data}
        renderItem={({item}) =>

        <View style={{backgroundColor:'#abc123',padding:10,margin:10}}>
          <Text style={{color:'#fff', fontWeight:'bold'}}>{item.Number}</Text>
          <Text style={{color:'#fff'}}>{item.Movement_data}</Text>
          </View>
        }

        />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
});