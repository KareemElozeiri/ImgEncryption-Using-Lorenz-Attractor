import {BrowserRouter, Routes, Route} from 'react-router-dom'
import { Suspense, lazy } from 'react';
import LoadingScreen from './Views/LoadingScreen';



const Main = lazy(()=>import('./Views/Main'))

function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<LoadingScreen/>}>
        <Routes>
          <Route exact path="/" element={ <Main/>} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}

export default App;