<template>
    <ItemTable :items="items" @show_add_modal="show_add_modal" @show_edit_modal="show_edit_modal"
        @update_table="updateTable" @show_email_modal="show_email_modal" />
    <AddItem :add_modal="add_modal" @hide_add_modal="hide_add_modal" @update_table="updateTable" />
    <EditItem :edit_modal="edit_modal" :edit_item="edit_item" @hide_edit_modal="hide_edit_modal"
        @update_table="updateTable" />
    <EmailModal :email_modal="email_modal" :email_link="email_link" @hide_email_modal="hide_email_modal" />
</template>
  
<script>
import ItemTable from './components/ItemTable.vue'
import AddItem from './components/AddItem.vue'
import EditItem from './components/EditItem.vue'
import EmailModal from './components/EmailModal.vue'

export default {
    name: 'HomePage',
    inject: ['api_base_url'],
    data() {
        return {
            items: [],
            add_modal: false,
            edit_modal: false,
            email_modal: false,
            edit_item: {},
            email_link: '',
        }
    },
    components: {
        ItemTable,
        AddItem,
        EditItem,
        EmailModal,
    },
    methods: {
        // function for getting items from the backend
        getItems() {
            fetch(this.api_base_url + '/backend/items')
                .then(response => response.json())
                .then(data => {
                    // convert date_added to a date object
                    data.forEach(item => {
                        item.date_added = new Date(item.date_added)
                    })

                    // convert difficulty to a number
                    data.forEach(item => {
                        item.difficulty = Number(item.difficulty)
                    })


                    this.items = data
                })
        },

        updateTable() {
            setTimeout(() => {
                this.getItems()
            }, 500)
        },

        // show add item modal
        show_add_modal() {
            this.add_modal = true
        },

        // hide add item modal
        hide_add_modal() {
            this.add_modal = false
        },

        // show edit item modal
        show_edit_modal(item) {
            console.log(item)
            this.edit_modal = true
            this.edit_item = item
        },

        // hide edit item modal
        hide_edit_modal() {
            this.edit_modal = false
        },

        // show email modal
        show_email_modal(link) {
            this.email_modal = true
            this.email_link = link
        },

        // hide email modal
        hide_email_modal() {
            this.email_modal = false
        },

    },
    mounted() {
        this.getItems()
    }

}

</script>

<style></style>