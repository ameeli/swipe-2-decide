import React, { Component } from "react";
import { render } from "react-dom";

class PriceRange extends Component {
  render() {
    return (
      <form name="priceRange">
        What's your price range?
        <input
          type="radio"
          name="range"
          value="1"
          onChange={this.props.onChange}
        />
        <label>$</label>
        <input
          type="radio"
          name="range"
          value="2"
          onChange={this.props.onChange}
        />
        <label>$$</label>
        <input
          type="radio"
          name="range"
          value="3"
          onChange={this.props.onChange}
        />
        <label>$$$</label>
        <input
          type="radio"
          name="range"
          value="4"
          onChange={this.props.onChange}
        />
        <label>$$$$</label>
      </form>
    );
  }
}

export default PriceRange;
