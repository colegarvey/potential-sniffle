import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, StyleSheet } from 'react-native';
import { fetchWorkouts } from '../services/api';

export default function HomeScreen() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    const loadWorkouts = async () => {
      try {
        const data = await fetchWorkouts();
        setWorkouts(data);
      } catch (error) {
        console.error('Failed to fetch workouts', error);
      }
    };

    loadWorkouts();
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>My Workouts</Text>
      <FlatList
        data={workouts}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View style={styles.workoutItem}>
            <Text style={styles.name}>{item.name}</Text>
            <Text style={styles.duration}>{item.duration_minutes} min</Text>
          </View>
        )}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, backgroundColor: '#fff' },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
  workoutItem: { padding: 10, borderBottomWidth: 1, borderBottomColor: '#ccc' },
  name: { fontSize: 18 },
  duration: { fontSize: 14, color: 'gray' },
});
