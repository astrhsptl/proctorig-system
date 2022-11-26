import Camera from "../components/Camera";
import HomePage from "../components/HomePage";
import LoginComponent from "../components/LoginComponent";
import RegiterComponent from "../components/RegiterComponent";
import SelfPage from "../components/SelfPage";


export const paths = [
    {path: '/', component: HomePage, exact: true},
    {path: '/login', component: LoginComponent, exact: true},
    {path: '/register', component: RegiterComponent, exact: true},
    {path: '/camera', component: Camera, exact: true},
    {path:'/account', component: SelfPage, exact: true}
];