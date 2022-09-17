import MainNavbar from "../Components/MainNavbar";
import "../Styles/Main.css"
import "bootstrap/dist/css/bootstrap.min.css"
import { Stack } from "react-bootstrap";
import Upload from "../Components/Upload";


const Main = ()=>{

    return(
        <div className="main">
            <MainNavbar/>
            <Stack>
                <Stack  style={{"padding":"50px"}}>
                    <h3>Encrypt</h3>
                    <hr/>
                    <Upload/>
                </Stack>


                <Stack style={{ "padding":"50px"}}>
                    <h3>Decrypt</h3>
                    <hr/>
                    <Upload/>
                </Stack>
            </Stack>
        
        </div>
    );
}

export default  Main;