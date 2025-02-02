# ShopWise

ShopWise is a web application that helps users find the best prices for ingredients needed to prepare their favorite meals. It utilizes web scraping to fetch ingredient prices from ShopRite, displays them with images, and allows users to add selected items to a shopping cart.

## Features

- **Ingredient Breakdown**: Enter a meal name, and the app retrieves its ingredients.
- **Price Comparison**: Fetches ingredient prices from ShopRite.
- **Sorting Options**: Sort items by price (high-to-low or low-to-high).
- **Shopping Cart**: Add items to a cart and manage them.
- **User-Friendly UI**: Clean and responsive design for ease of use.

## Technologies Used

- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript (Jinja templating)
- **Data Handling**: BeautifulSoup for web scraping
- **APIs**: OpenAI API for ingredient extraction

## Installation

### Prerequisites

- Python 3.8+
- `pip` (Python package manager)

### Setup

1. **Clone the repository**:

   ```sh
   git clone https://github.com/your-repo/shopwise.git
   cd shopwise

   ```

2. **Create a virtual environment (optional but recommended)**:

   ```sh
   python -m venv venv
   source venv/bin/activate

   ```

3. **Install dependencies**:

   ```sh
   pip install -r requirements.txt

   ```

4. **Set up environment variables**:

- Create a .env file and add your OpenAI API key:
  ```sh
  OPENAI_API_KEY=your-api-key
  ```

5. **Run the Application**:

   ```sh
   python app.py

   ```

6. **Open the browswer and visit**:
   http://127.0.0.1:5001/

## Usage

- Enter a meal name in the search box.
- View the ingredient list and their prices.
- Select items and add them to the shopping cart.
- Manage your cart (view, remove items).
- Proceed to purchase (handled externally).

## Future Enhancements

- Add more grocery stores for price comparison.
- Implement user authentication for saved carts.
- Introduce a recipe suggestion feature.

## Contributors

Samarth Verma - MaybeSam05
Dhruv Agarwal - DhruvNA05
Gravit Bali - GravitB
Sai Suhas Chekka - SSC

#### Contributions welcome! Feel free to submit pull requests.

# Enjoy and Shop Wise!