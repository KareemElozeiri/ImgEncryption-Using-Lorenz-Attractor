import React from 'react';
import { Container, Navbar } from 'react-bootstrap';
import "bootstrap/dist/css/bootstrap.min.css"


const MainNavbar = ()=>{
    return (
        <Navbar className="navbar  border-bottom border-secondary" style={{"color":"#6c4a7d","borderColor":"#6c4a7d"}} expand="lg">
            <Container>
                <Navbar.Brand href="/" style={{"color":"#6c4a7d"}}> <h1 className="logo-icon"> Lorenz</h1></Navbar.Brand>
            
            </Container>
            
        </Navbar>
      );
}


export default MainNavbar;