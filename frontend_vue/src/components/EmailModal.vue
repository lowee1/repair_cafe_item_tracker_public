<template>
    <b-modal v-model="local_modal" hide-footer>
        <b-button v-on:click="openLink">
        Click here to open the email in your default browser mail client</b-button>
        <p style="font-size: small;">This will open in a new tab. If that page doesn't load you may have to reload the page.</p>
    </b-modal>
</template>

<script>
export default {
    name: 'EmailModal',
    data() {
        return {
            local_modal: false,
            local_link: '',
        }
    },
    props: {
        email_modal: {
            type: Boolean,
            required: true
        },
        email_link: {
            type: String,
            required: true
        }
    },
    watch: {
        email_modal: function (newVal) {
            this.local_modal = newVal
        },
        email_link: function (newVal) {
            this.local_link = newVal
        }
    },
    methods: {
        openLink() {
            // open mailto link in a new tab
            window.open(this.local_link, '_blank')
        }
    }
}

</script>
