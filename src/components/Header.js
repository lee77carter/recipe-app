import React from "react";
import { Search } from "react-feather";
import { ReactComponent as Logo } from "../images/utensils.svg";

const Header = ({ showRecipeForm, searchTerm, updateSearchTerm }) => {
  return (
    <header>
      <div className='logo-search'>
        <Logo />
        <div className='search'>
          <label className='visually-hidden' htmlFor='search'>
            Search
          </label>
          <input
            type='text'
            placeholder='Search'
            id='search'
            value={searchTerm}
            onChange={(e) => updateSearchTerm(e.target.value)}
          />
          <Search />
        </div>
      </div>
      <h1>My Favorite Recipes</h1>
      <button className='new-recipe' onClick={showRecipeForm}>
        Add New Recipe
      </button>
    </header>
  );
};

export default Header;