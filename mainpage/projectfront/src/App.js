import logo from './logo.svg';
import arrow from './assets/images/fast-forward.png';
import './App.css';

function App() {
  const imageUrl = `${window.staticUrl}images/fast-forward.png`;
  return (
    <div class="container-fluid" id="app-container" >
    <h1>Check out my work and see which project you'd want to <b>'buy'</b> into!</h1>
    <button><img src={imageUrl} alt="Fast Forward" />
    </button>
</div>
  );
}

export default App;
