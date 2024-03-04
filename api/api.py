'''An app written in both Python & JavaScript. This recipe app is built with a backend Flask web application (api/api.py - Python web framework), and the frontend using React (src/App.js), which consumes and interacts with the API created. 
The recipes are loaded and saved to a database, with SHOW, CREATE, UPDATE, and DELETE capabilities.'''

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
db = SQLAlchemy(app)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(500), nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True,
                            default='Delicious. You need to try it!')
    image_url = db.Column(db.String(500), nullable=True,
                          default="https://images.pexels.com/photos/9986228/pexels-photo-9986228.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
    servings = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Recipe(id={self.id}, title='{self.title}', description='{self.description}', servings={self.servings})"

# with app.app_context():
#     db.create_all()
#     db.session.commit()

# Route to fetch all recipes


@app.route('/api/recipes', methods=['GET'])
def get_all_recipes():
    recipes = Recipe.query.all()
    recipe_list = []
    for recipe in recipes:
        recipe_list.append({
            'id': recipe.id,
            'title': recipe.title,
            'ingredients': recipe.ingredients,
            'instructions': recipe.instructions,
            'description': recipe.description,
            'image_url': recipe.image_url,
            'servings': recipe.servings
        })
    return jsonify(recipe_list)

# Route to add a new recipe


@app.route('/api/recipes', methods=['POST'])
def add_recipe():
    data = request.get_json()
    # Validate the incoming JSON data for required fields
    required_fields = ['title', 'ingredients',
                       'instructions', 'servings', 'description', 'image_url']

    for field in required_fields:
        if field not in data or data[field] == "":
            return jsonify({'error': f"Missing required field: '{field}'"}), 400

    new_recipe = Recipe(
        title=data['title'],
        ingredients=data['ingredients'],
        instructions=data['instructions'],
        servings=data['servings'],
        description=data['description'],
        image_url=data['image_url']
    )

    db.session.add(new_recipe)
    db.session.commit()

    # Serialize the new recipe and return it as JSON
    new_recipe_data = {
        'id': new_recipe.id,
        'title': new_recipe.title,
        'ingredients': new_recipe.ingredients,
        'instructions': new_recipe.instructions,
        'servings': new_recipe.servings,
        'description': new_recipe.description,
        'image_url': new_recipe.image_url
    }

    return jsonify({'message': 'Recipe added successfully', 'recipe': new_recipe_data})

# Route to update a recipe


@app.route('/api/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return jsonify({'error': 'Recipe not found'}), 404

    data = request.get_json()

    # Validate the incoming JSON data for required fields
    required_fields = ['title', 'ingredients',
                       'instructions', 'servings', 'description', 'image_url']

    for field in required_fields:
        if field not in data or data[field] == "":
            return jsonify({'error': f"Missing required field: '{field}'"}), 400

    recipe.title = data['title']
    recipe.ingredients = data['ingredients']
    recipe.instructions = data['instructions']
    recipe.servings = data['servings']
    recipe.description = data['description']
    recipe.image_url = data['image_url']

    db.session.commit()
 # Serialize the updated recipe and return it as JSON
    updated_recipe = {
        'id': recipe.id,
        'title': recipe.title,
        'ingredients': recipe.ingredients,
        'instructions': recipe.instructions,
        'servings': recipe.servings,
        'description': recipe.description,
        'image_url': recipe.image_url
    }

    return jsonify({'message': 'Recipe updated successfully', 'recipe': updated_recipe})

# Route to delete a recipe


@app.route('/api/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return jsonify({'error': 'Recipe not found'}), 404

    db.session.delete(recipe)
    db.session.commit()
    return jsonify({'message': 'Recipe deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)