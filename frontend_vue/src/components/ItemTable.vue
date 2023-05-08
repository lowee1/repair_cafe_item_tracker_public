<template>
    <!-- tool box -->
    <b-button-toolbar key-nav id="button-tools">
        <!-- search box -->
        <b-button-group id="search-button-group">
            <b-form inline id="item-search-form" @reset="onReset">
                <b-form-input id="search-box" type="text" placeholder="Type to search" v-model="search"></b-form-input>

                <b-dropdown id="search-filter-select-dropdown-container" no-caret>
                    <template #button-content>
                        <Icon icon="carbon:filter"></Icon>
                    </template>

                    <b-form-select id="search-filter-select" v-model="filter" multiple>
                        <b-form-select-option v-for="field in headers" :value="field.value" :key="field.value">{{
                            field.text
                        }}</b-form-select-option>
                    </b-form-select>
                </b-dropdown>

                <b-button type="reset" variant="outline-dark">
                    <Icon icon="carbon:reset"></Icon>
                </b-button>
            </b-form>
        </b-button-group>

        <b-button-group>
            <b-form>
                <!-- hurry up button -->
                <b-button id="hurryUpButton" variant="outline-light" @click="hurry_up()">
                    <Icon icon="carbon:warning-alt"></Icon>
                </b-button>

                <!-- delete button -->
                <b-button id="deleteButton" variant="outline-light" @click="show_delete_modal()">
                    <Icon icon="carbon:delete"></Icon>
                </b-button>

                <!-- edit item button -->
                <b-button id="editButton" variant="outline-dark" @click="show_edit_modal()">
                    <Icon icon="carbon:edit"></Icon>
                </b-button>

                <!-- add item button -->
                <b-button id="addButton" variant="outline-light" @click="show_add_modal()">
                    <Icon icon="carbon:add-alt"></Icon>
                </b-button>

                <!-- email button -->
                <b-button id="emailButton" variant="outline-light" @click="show_email_modal()">
                    <Icon icon="carbon:email"></Icon>
                </b-button>

            </b-form>
        </b-button-group>

    </b-button-toolbar>
    <p v-if="search">Searching for: "{{ search }}" in {{ filter ? filter.join(', ') : "all fields" }}</p>

    <EasyDataTable :headers="headers" :items="items" table-class-name="customize-table"
        :body-row-class-name="bodyRowClassNameFunction" :search-value="search" :search-field="filter"
        v-model:items-selected="itemsSelected" fixed-checkbox :checkbox-column-width="36" alternating>
        <template #item-image="{ image }">
            <b-img class="table-image" :src="image" left lazy />
        </template>
    </EasyDataTable>

    <b-modal id="delete-confirm-modal" title="Confirm Delete" @ok="delete_selected()" v-model="deleteModal">
        <p>Are you sure you want to delete the selected items?</p>
    </b-modal>
</template>

<script>
import { Icon } from '@iconify/vue';

export default {
    name: 'ItemTable',
    inject: ['api_base_url'],
    data() {
        return {
            headers: [
                { text: "Item", value: "item", sortable: true },
                { text: "Problem", value: "problem", sortable: true },
                { text: "Owner", value: "owner", sortable: true },
                { text: "Date Added", value: "date_added", width: 200, sortable: true },
                { text: "Status", value: "status", sortable: true },
                { text: "Assignee", value: "assigned_to", sortable: true },
                { text: "Difficulty", value: "difficulty", sortable: true },
                { text: "Image", value: "image", sortable: true },
                { text: "Urgency", value: "hurry_count", sortable: true },
            ],
            search: '',
            filter: '',
            itemsSelected: [],
            deleteModal: false,
        }
    },
    props: {
        items: {
            type: Array,
            required: true
        },
    },
    components: {
        Icon,
    },
    methods: {
        // form reset
        onReset(evt) {
            evt.preventDefault()
            this.search = ''
            this.filter = ''
        },
        bodyRowClassNameFunction(item) {
            if (item.hurry_count <= 3) {
                // table-hurry-{number}
                return 'table-hurry-' + item.hurry_count;
            }
            else {
                return 'table-hurry-4';
            }

        },

        // show add item modal
        show_add_modal() {
            this.$emit('show_add_modal');
        },

        show_edit_modal() {
            // make sure only one item selected
            if (this.itemsSelected.length == 1) {
                // emit event to show edit modal
                this.$emit('show_edit_modal', this.itemsSelected[0]);
            }
            else {
                alert("Please select one item to edit");
            }
        },

        show_delete_modal() {
            // check if any items selected first
            if (this.itemsSelected.length > 0) {
                this.deleteModal = true;
            }
            else {
                alert("No items selected");
            }
        },

        delete_selected() {
            for (let item in this.itemsSelected) {
                // get id of item
                let id = this.itemsSelected[item].id;

                // delete item from database
                fetch(this.api_base_url + '/backend/items/' + id + '/', {
                    method: 'DELETE',
                })
                    .then(response => response.json())
                    .then(data => {
                        console.log('Success:', data);
                    })
                    .catch((error) => {
                        console.error('Error:', error);
                    });
            }

            this.itemsSelected = [];

            // emit event to update table
            this.$emit('update_table');

        },

        hurry_up() {
            // get the items
            let items = this.itemsSelected;

            // check if any items selected
            if (items.length > 0) {
                // loop through items
                for (let item in items) {
                    // get id of item
                    let id = items[item].id;

                    // update item in database
                    fetch(this.api_base_url + '/backend/items/' + id + '/', {
                        method: 'PATCH',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            "hurry_count": items[item].hurry_count + 1,
                        }),
                    })
                }

                // emit event to update table
                this.$emit('update_table');
            }
            else {
                alert("No items selected");
            }
        },
        generate_email(data) {
            // get the owner_email, item, owner name, status, and assigned_to
            let owner_email = data.owner_email;
            let item = data.item;
            let owner = data.owner;
            let status = data.status;
            let assigned_to = data.assigned_to;

            // create the title
            let title = "Repair Cafe Item: " + item + ", Status: " + status;

            // create the body using the template
            let body = `Dear ${owner},%0D%0A%0D%0AThe status of your item, ${item}, has been updated to ${status}.%0D%0A%0D%0AIf you have any questions, please contact ${assigned_to}.%0D%0A%0D%0AThank you,%0D%0ARepair Cafe%0D%0A`;

            return [owner_email, title, body];
        },
        show_email_modal() {
            // check if any items selected first
            if (this.itemsSelected.length == 0) {
                alert("No items selected");
                return;
            }

            // for each item, pass the id to the email generator to get the title and content
            // then pass the title and content to the email modal
            for (let item of this.itemsSelected) {
                // get id of item
                let id = item.id;

                let owner_email, title, body;

                // get item from database
                fetch(this.api_base_url + '/backend/items/' + id + '/', {
                    method: 'GET',
                })
                    .then(response => response.json())
                    .then(data => {
                        console.log("data", data);

                        // check if there is an owner_email
                        if (data.owner_email == null) {
                            alert("No owner_email for item " + data.item);
                            return;
                        }

                        [owner_email, title, body] = this.generate_email(data);

                        // create a mailto link
                        let link = "mailto:" + owner_email + "?subject=" + title + "&body=" + body;

                        // pass the link to the email modal
                        this.$emit('show_email_modal', link);
                    })
                    .catch((error) => {
                        console.error('Error:', error);
                    });
            }
        },

    },
    emits: ['show_add_modal', 'update_table', 'show_edit_modal', 'show_email_modal'],
}
</script>

<style>
.customize-table {
    --easy-table-body-row-height: 100px;
    width: 100%;
}

.table-image {
    height: 100px;
    max-width: 200px;
}

#search-button-group {
    display: flex;
    flex-grow: 2;
    max-width: 50%;
}

#item-search-form {
    display: flex;
    flex-direction: row;
    flex-grow: 1;
}

#search-box {
    display: flex;
    flex-grow: 3;
}

#search-filter-select {
    display: flex;
    flex-grow: 1;
    height: 100%;
}

.dropdown-menu.show {
    display: flex;
    padding: 0px;
    height: 200px;
}

#button-tools {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 100%;
    align-items: center;
    padding: 0.5rem;
}

#deleteButton {
    background-color: red;
}

#addButton {
    background-color: green;
}

#hurryUpButton {
    background-color: orange;
}

#emailButton {
    background-color: blue;
}

.table-hurry-0 {
    --easy-table-row-border: 6px solid #ffffff;
    --easy-table-body-row-font-color: #000000;
}

.table-hurry-1 {
    --easy-table-row-border: 6px solid #f4f593;
}

.table-hurry-2 {
    --easy-table-row-border: 6px solid #eeff00;
}

.table-hurry-3 {
    --easy-table-row-border: 6px solid #f93939;
}

.table-hurry-4 {
    --easy-table-row-border: 6px solid #ff0000;
}
</style>