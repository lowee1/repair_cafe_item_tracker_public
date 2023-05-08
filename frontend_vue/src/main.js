import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import BootstrapVueNext from "bootstrap-vue-next";

import Vue3EasyDataTable from "vue3-easy-data-table";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue-next/dist/bootstrap-vue-next.css";
import "vue3-easy-data-table/dist/style.css";

import App from "./App.vue";
import HomePage from "./HomePage.vue";
import AboutPage from "./AboutPage.vue";
import ContactPage from "./ContactPage.vue";

const routes = [
  { path: "/", component: HomePage },
  { path: "/about", component: AboutPage },
  { path: "/contact", component: ContactPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

const app = createApp(App);

app.use(BootstrapVueNext);
app.use(router);
app.component("EasyDataTable", Vue3EasyDataTable);
app.provide(
  "api_base_url",
  "<redacted>"
);
app.mount("#app");
