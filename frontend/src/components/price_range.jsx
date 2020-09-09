import React, { Component } from "react";
import { render } from "react-dom";

class PriceRange extends Component {
  render() {
    return (
      <div>
        <button>$</button>
        <button>$$</button>
        <button>$$$</button>
        <button>$$$$</button>
      </div>
    );
  }
}

export default PriceRange;
