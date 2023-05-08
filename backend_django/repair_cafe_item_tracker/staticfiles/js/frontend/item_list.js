console.log("item_list.js");

const item_list_url = request_uri + "backend/items.json";
// get the list of items and display them
fetch(item_list_url)
  .then((response) => response.json())
  .then((data) => {
    console.log(data);
    const table = document
      .getElementById("item-table")
      .getElementsByTagName("tbody")[0];
    // clear the table except for the header
    while (table.children.length > 1) {
      table.removeChild(table.lastChild);
    }

    // count the number of items
    const num_items = data.length;

    // add each item to the table
    data.forEach((item) => {
      console.log(item);
      // create the row item
      const row = document.createElement("tr");
      row.classList.add("item-row");

      // create the item name
      const name = document.createElement("td");
      name.innerText = item.item;

      // create the item owner
      const owner = document.createElement("td");
      owner.innerHTML = item.owner + "<br>(" + item.email + ")";

      // create the item description
      const description = document.createElement("td");
      description.innerText = item.problem;

      // create the image
      const image_td = document.createElement("td");
      const image = document.createElement("img");
      image.src = item.image
        ? item.image
        : "https://via.placeholder.com/150?text=No+Image";

      // add the image to the image td
      image_td.appendChild(image);

      // add to the row item
      row.appendChild(name);
      row.appendChild(owner);
      row.appendChild(description);
      row.appendChild(image_td);

      // add the list item to the table
      table.appendChild(row);

      // set the table height to the number of items * 100px
      table.style.height = (num_items * 100).toString() + "px";
    });
  });
