import { Button, Stack } from "react-bootstrap";
import Figure from 'react-bootstrap/Figure';


const RecieveBox = ()=>{

    return (
        <div className="recieve-box">
            <Stack>
                <Figure>
                        <Figure.Image
                            width={400}
                            height={400}
                            alt="400x400"
                            style={{"border":"1px #6c4a7d"}}
                            src="holder.js/400x400"

                        />
                </Figure>
                <Button style={{"backgroundColor":"#6c4a7d","color":"white"}}>Download</Button>
            </Stack>
        </div>
    );
}


export default RecieveBox;