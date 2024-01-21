import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import logo2 from '../Components/images/logo.jpeg'


function PizzasForm() {
  const [pizzas, setPizzas] = useState([]);
  const [pizzaId, setPizzaId] = useState("");
  const [restaurants, setRestaurants] = useState([]);
  const [restaurantId, setRestaurantId] = useState("");
  const [price, setPrice] = useState("");
  const [formErrors, setFormErrors] = useState([]);
  const navigate = useNavigate(); 

  useEffect(() => {
    fetch("/pizzas")
      .then((r) => r.json())
      .then(setPizzas);
  }, []);

  useEffect(() => {
    fetch("/restaurants")
      .then((res) => res.json())
      .then(setRestaurants);
  }, []);

  function handleSubmit(e) {
    e.preventDefault();
    const formData = {
      pizza_id: pizzaId,
      restaurant_id: restaurantId,
      price: parseInt(price),
    };
    fetch("/restaurant_pizzas", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((r) => {
        if (r.ok) {
          navigate("/");
        } else {
          r.json().then((err) => setFormErrors(err.errors));
        }
      })
      .catch((error) => {
        console.error("Error adding pizza to restaurant:", error);
      });
  }

  return (
    <div className="bg-primary text-white p-5" style={{ backgroundImage: `url(${logo2})` }}>
    <img src="logo2" class="img-fluid" alt=""></img>

      <form onSubmit={handleSubmit} className="mt-4">
        <div className="form-group">
          <label htmlFor="price">Price:</label>
          <input
            type="number"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
            className="form-control"
          />
        </div>

        <div className="form-group">
          <label htmlFor="pizzaId">Select Pizza:</label>
          <select
            id="pizzaId"
            name="pizzaId"
            value={pizzaId}
            onChange={(e) => setPizzaId(e.target.value)}
            className="form-control"
          >
            <option value="">Select a pizza</option>
            {pizzas.map((pizza) => (
              <option key={pizza.id} value={pizza.id}>
                {pizza.name}
              </option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="restaurantId">Select Restaurant:</label>
          <select
            id="restaurantId"
            name="restaurantId"
            value={restaurantId}
            onChange={(e) => setRestaurantId(e.target.value)}
            className="form-control"
          >
            <option value="">Select a restaurant</option>
            {restaurants.map((restaurant) => (
              <option key={restaurant.id} value={restaurant.id}>
                {restaurant.name}
              </option>
            ))}
          </select>
        </div>

        {formErrors.length > 0 &&
          formErrors.map((err, index) => (
            <p key={index} style={{ color: "red" }}>
              {err}
            </p>
          ))}

        <button type="submit" className="btn btn-primary">
          Add To Restaurant
        </button>
      </form>
    </div>
  );
}

export default PizzasForm;
