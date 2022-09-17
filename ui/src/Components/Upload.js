import Form from 'react-bootstrap/Form';
import Stack from 'react-bootstrap/Stack';
import "../Styles/Upload.css";

const Upload = ()=>{

    return (
        <div className='upload'>
            <Stack>
                <Form.Control type="file" size="lg" />
            </Stack>
        </div>
    );
}


export default Upload;