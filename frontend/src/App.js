import React, { Component } from "react";
import { render } from "react-dom";
import PriceRange from "./components/price_range";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      priceRange: null,
      restaurants: [],
      loaded: false,
      placeholder: "Loading",
    };
  }

  componentDidMount() {
    fetch("api/find_restaurants/")
      .then((response) => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then((restaurants) => {
        this.setState(() => {
          return {
            restaurants,
            loaded: true,
          };
        });
      });
  }

  handlePriceRangeChange = (changeEvent) => {
    this.setState({ priceRange: changeEvent.target.value });
  };

  render() {
    return (
      <React.Fragment>
        <PriceRange onChange={this.handlePriceRangeChange} />
        {this.state.priceRange}
        {/*
        <ul>
          {this.state.restaurants.map((restaurant) => {
            return (
              <li key={restaurant.id}>
                {restaurant.name} - {restaurant.rating}
              </li>
            );
          })}
        </ul>
*/}
      </React.Fragment>
    );
  }
}

export default App;
