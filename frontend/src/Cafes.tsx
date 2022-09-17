import React, { useEffect, useState } from 'react';
import './Cafes.css';

interface ServerCafe {
  name: string,
  address: string,
  features: Map<string, string>
}

export function Cafes() {
  const [cafes, setCafes] = useState<ServerCafe[]>([])

  const fetchCafes = () => {
    fetch('http://localhost:8000/cafes')
    .then((response) => response.json())
    .then(cafesList => {
      setCafes(cafesList)
    })
  }

  fetchCafes()

  return (
    <div className="Cafes">
      {cafes.map((cafe) => {
        return (<div>{cafe.name}</div>)
      })}
    </div>
  );
}

