import React from 'react';
import { Card } from 'antd';
import { Cafe } from './types';

interface CafeProps {
    cafe: Cafe
}

export function CafeCard({ cafe }: CafeProps) {
    return (<div>
        <Card title={cafe.name} extra={<a href="#">Reviews</a>} style={{ width: 300 }}>
          <p>Card content</p>
          <p>Card content</p>
          <p>Card content</p>
        </Card>
    </div>)
}
