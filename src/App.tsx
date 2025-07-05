import React, { useState } from 'react';
import Header from './components/Header';
import Hero from './components/Hero';
import CVForm from './components/CVForm';

function App() {
  const [showForm, setShowForm] = useState(false);

  const handleStartBuilding = () => {
    setShowForm(true);
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      {!showForm ? (
        <div>
          <Hero onStartBuilding={handleStartBuilding} />
          <div className="text-center py-12">
            <button
              onClick={handleStartBuilding}
              className="bg-gradient-to-r from-blue-500 to-indigo-600 text-white px-8 py-4 rounded-lg font-semibold hover:from-blue-600 hover:to-indigo-700 transition-all transform hover:scale-105 shadow-lg"
            >
              Get Started - Build Your CV
            </button>
          </div>
        </div>
      ) : (
        <div className="py-12">
          <CVForm />
        </div>
      )}
    </div>
  );
}

export default App;