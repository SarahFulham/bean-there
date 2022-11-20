import { useEffect, useState } from 'react';
import { CafeCard } from './CafeCard';
import './Cafes.css';
import { Cafe } from './types';

export function Cafes() {
  const [cafes, setCafes] = useState<Cafe[]>([])

  const fetchCafes = () => {
    fetch('http://localhost:8000/cafes')
    .then((response) => response.json())
    .then(cafesList => {
      setCafes(cafesList)
    })
  }


  useEffect(() => {
    fetchCafes()
  }, [])

  return (
    <div className="Cafes">
      {cafes.map((cafe) => {
        return (<CafeCard key={cafe.id} cafe={cafe}/>)
      })}
    </div>
  );
}

