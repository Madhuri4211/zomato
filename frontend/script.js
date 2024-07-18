const restaurantListElement = document.getElementById('restaurant-list');
const paginationElement = document.getElementById('pagination');
const itemsPerPage = 100; // Display 100 restaurants per page
let currentPage = 1;
let totalItems = 0;

function fetchRestaurants(page = 1) {
  fetch(`http://127.0.0.1:8000/restaurants?skip=${(page - 1) * itemsPerPage}&limit=${itemsPerPage}`)
    .then(response => response.json())
    .then(data => {
      totalItems = data.total;
      renderRestaurants(data.items);
      renderPagination();
    })
    .catch(error => console.error('Error fetching restaurants:', error));
}

function renderRestaurants(restaurants) {
  restaurantListElement.innerHTML = '';
  restaurants.forEach(restaurant => {
    const restaurantContainer = document.createElement('div');
    restaurantContainer.classList.add('restaurant-container'); // Container for each restaurant item

    const restaurantName = document.createElement('div');
    restaurantName.textContent = restaurant.restaurant_name;
    restaurantName.classList.add('restaurant-item'); // Add CSS class for styling
    restaurantName.dataset.menuUrl = restaurant.menu_url; // Store menu_url in data attribute
    restaurantName.addEventListener('click', function() {
      const menuUrl = this.dataset.menuUrl;
      console.log(`Redirecting to ${menuUrl}`); // Debugging line to ensure menuUrl is set
      alert(`Redirecting to ${menuUrl}`); // Add alert to ensure the click is registering
      window.location.href = menuUrl; // Redirect to menu_url on click
    });

    const restaurantImage = document.createElement('img');
    restaurantImage.src = restaurant.featured_image;
    restaurantImage.alt = `${restaurant.restaurant_name} image`;
    restaurantImage.classList.add('restaurant-image'); // Add CSS class for styling

    restaurantContainer.appendChild(restaurantImage);
    restaurantContainer.appendChild(restaurantName);
    restaurantListElement.appendChild(restaurantContainer);
  });
}

function renderPagination() {
  paginationElement.innerHTML = '';
  const totalPages = Math.ceil(totalItems / itemsPerPage);

  // Previous Button
  const prevButton = document.createElement('button');
  prevButton.textContent = 'Previous';
  prevButton.addEventListener('click', function() {
    if (currentPage > 1) {
      currentPage--;
      fetchRestaurants(currentPage);
    }
  });
  paginationElement.appendChild(prevButton);

  // Next Button
  const nextButton = document.createElement('button');
  nextButton.textContent = 'Next';
  nextButton.addEventListener('click', function() {
    if (currentPage < totalPages) {
      currentPage++;
      fetchRestaurants(currentPage);
    }
  });
  paginationElement.appendChild(nextButton);
}

document.addEventListener('DOMContentLoaded', () => {
  fetchRestaurants(currentPage);
});
