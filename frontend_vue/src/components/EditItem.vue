<template>
    <b-modal v-model="local_modal" hide-footer>
        <h1>Edit an item</h1>
        <p>You only need to enter data into fields which you wish to edit. All empty fields will retain their previous
            values.</p>
        <b-form @submit.stop.prevent="submit">

            <b-form-group label="Item" label-for="item">
                <b-form-input id="item" v-model="item" placeholder="Enter item name"></b-form-input>
            </b-form-group>

            <b-form-group label="Problem" label-for="problem">
                <b-form-input id="problem" v-model="problem" placeholder="Enter problem description"></b-form-input>
            </b-form-group>

            <b-form-group label="Owner" label-for="owner">
                <b-form-input id="owner" v-model="owner" placeholder="Enter owner name"></b-form-input>
            </b-form-group>

            <b-form-group label="Owner Email" label-for="owner_email">
                <b-form-input id="owner_email" v-model="owner_email" placeholder="Enter owner email" type="email"
                    :state="owner_email_valid"></b-form-input>
            </b-form-group>

            <b-form-group label="Status" label-for="status">
                <b-form-select id="status" v-model="status" required>
                    <b-form-select-option value="Unassigned">Unassigned</b-form-select-option>
                    <b-form-select-option value="In progress">In progress</b-form-select-option>
                    <b-form-select-option value="Nearly Done">Nearly Done</b-form-select-option>
                    <b-form-select-option value="Testing">Testing</b-form-select-option>
                    <b-form-select-option value="Done">Done</b-form-select-option>
                    <b-form-select-option value="More broken than before">More broken than before</b-form-select-option>
                    <b-form-select-option value="Completely broken, beyond repair">Completely broken, beyond
                        repair</b-form-select-option>
                    <b-form-select-option value="Awaiting resources">Awaiting resources</b-form-select-option>
                </b-form-select>
            </b-form-group>

            <b-form-group label="Assignee" label-for="assigned_to">
                <b-form-input id="assigned_to" v-model="assigned_to" placeholder="Enter assignee name"></b-form-input>
            </b-form-group>

            <b-form-group label="Difficulty" label-for="difficulty">
                <b-form-input id="difficulty" v-model="difficulty" placeholder="Enter difficulty" type="number" min="0"
                    max="10"></b-form-input>
            </b-form-group>

            <b-form-group label="Image" label-for="image">
                <!-- upload image file -->
                <input type="file" id="image" name="image" accept="image/png,image/jpeg" @change="uploadImage">
            </b-form-group>

            <b-form-group>
                <b-button type="submit" variant="primary" @click="patch_item">Submit</b-button>
                <b-button variant="danger" @click="local_modal = false">Cancel</b-button>
            </b-form-group>
        </b-form>
    </b-modal>
</template>

<script>
export default {
    name: 'EditItem',
    inject: ['api_base_url'],
    data() {
        return {
            local_modal: false,
            item: '',
            problem: '',
            owner: '',
            owner_email: '',
            date_added: '',
            status: '',
            assigned_to: '',
            difficulty: '',
            image: '',
        }
    },
    props: {
        edit_modal: {
            type: Boolean,
            required: true
        },
        edit_item: {
            type: Object,
            required: true
        }
    },
    methods: {
        uploadImage(event) {
            // get the image file
            this.image = event.target.files[0]
        },
        async patch_item() {
            // build the form data
            // only add the fields which have been edited
            let formData = new FormData()
            let reader = new FileReader()
            if (this.item !== '')
                formData.append('item', this.item)
            if (this.problem !== '')
                formData.append('problem', this.problem)
            if (this.owner !== '')
                formData.append('owner', this.owner)
            if (this.owner_email !== '')
                formData.append('owner_email', this.owner_email)
            if (this.date_added !== '')
                formData.append('date_added', this.date_added)
            if (this.status !== '')
                formData.append('status', this.status)
            if (this.assigned_to !== '')
                formData.append('assigned_to', this.assigned_to)
            if (this.difficulty !== '')
                formData.append('difficulty', this.difficulty)

            if (this.image instanceof File) {
                reader.addEventListener("load", function () {
                    formData.append('image', reader.result)
                }, false);

                // make a copy of the image file data into base64 representation
                reader.readAsDataURL(this.image);

                // wait until done
                while (reader.readyState !== 2) { 
                    console.log("waiting for reader", reader.readyState, reader.result)

                    if (reader.readyState === 2) {
                        console.log("done")
                        break
                    }

                    await new Promise(r => setTimeout(r, 100));
                }
            }

            // log all form data
            console.log(1)
            for (var input of formData.entries()) {
                console.log(input[0] + ': ' + input[1]);
            }

            // send the form data to the server
            fetch(this.api_base_url + "/backend/items/" + this.edit_item.id + '/', {
                method: 'PATCH',
                body: formData
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    this.local_modal = false
                })
                .catch(error => {
                    console.error(error)
                })

            // emit the event to update the list
            this.$emit('update_table')
        },
    },
    watch: {
        edit_modal: function (newVal) {
            if (newVal !== this.local_modal) {
                this.local_modal = newVal
            }
        },
        local_modal: function (newVal) {
            if (!newVal) {
                this.$emit('hide_edit_modal')
            }
        }

    },
    computed: {
        // form validation
        owner_email_valid() {
            return this.owner_email === '' || this.owner_email.includes('@')
        },
    },
    emits: ['hide_edit_modal', 'update_table'],
}

</script>

<style></style>
