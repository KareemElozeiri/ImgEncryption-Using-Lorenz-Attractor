import MainNavbar from "../Components/MainNavbar";
import "../Styles/Main.css"
import "bootstrap/dist/css/bootstrap.min.css"
import { Button, Stack } from "react-bootstrap";
import Upload from "../Components/Upload";
import { useState } from "react";
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import ToggleButton from 'react-bootstrap/ToggleButton';
import Image from "react-bootstrap/Image";
import RecieveBox from "../Components/RecieveBox";


const Main = ()=>{


    const [mode, setMode] = useState('0')
    const radios = [
        {name:"Encrypt",value:'0'},
        {name:"Decrypt", value:'1'  }
    ]
    return(
        <div className="main">
            <MainNavbar/>

            <div style={{"textAlign":"center","padding":"1%"}}>
                <ButtonGroup style={{"margin":"auto"}}>
                {radios.map((radio, idx) => (
                <ToggleButton
                    style={(mode===radio.value)?{"backgroundColor":"#6c4a7d","color":"white","border":"#6c4a7d"}:{"color":"#6c4a7d","backgroundColor":"white","border":" 1px #6c4a7d"}}
                    key={idx}
                    id={`radio-${idx}`}
                    type="radio"
                    name="radio"
                    value={radio.value}
                    checked={mode === radio.value}
                    onChange={(e) => setMode(e.currentTarget.value)}
                >
                    {radio.name}
                </ToggleButton>
                ))}
                </ButtonGroup>
            </div>

            <Stack style={{"padding":"1%"}}>
                <h3>{mode==='1'?"Decrypt":"Encrypt"} :</h3>
                <hr/>
                <Stack direction="horizontal" style={{"width":"80%","margin":"auto"}}>
                    <Upload/>
                    <RecieveBox/>
                </Stack>
                <Button style={{"alignSelf":"center","backgroundColor":"#6c4a7d","color":"white","width":"20%"}}>Execute</Button>
            </Stack>


        
        </div>
    );
}

export default  Main;