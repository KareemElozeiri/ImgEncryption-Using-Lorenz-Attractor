import Form from 'react-bootstrap/Form';
import Stack from 'react-bootstrap/Stack';
import "../Styles/Upload.css";
import Figure from 'react-bootstrap/Figure';
import 'holderjs'
const Upload = ()=>{

    return (
        <div className='upload'>
            <Stack>
                <Figure style={{"border":"1px #6c4a7d"}}>
                    <Figure.Image
                        width={400}
                        height={400}
                        alt="400x400"
                        src="holder.js/400x400"
                        style={{"alignSelf":"center"}}
                    />
                </Figure>
                <Form.Control type="file" style={{"width":"50%"}} />
            </Stack>
        </div>
    );
}


export default Upload;