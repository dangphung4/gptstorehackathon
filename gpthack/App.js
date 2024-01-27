import { StatusBar } from "expo-status-bar";
import {
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
  TextInput,
} from "react-native";
import React, { useState } from "react";
import { themeColors } from "./ThemeProvider";
//import TextInput from "react-native-text-input-interactive";

export default function App() {
  const [songQuery, setSongQuery] = useState("");
  const [isDarkMode, setIsDarkMode] = useState(true);
  const [gptQuery, setGptQuery] = useState("");

  const handleSearch = () => {
    // Implement the logic for searching and recommending music based on the songQuery
    // You can make an API call or perform some AI-related operations here
    console.log(`Searching for music based on: ${songQuery}`);

    // then clear input field
    setSongQuery("");
  };

  const handleGptSearch = () => {
    // Implement the logic for handling the GPT search when the input is submitted
    console.log(`Handling GPT search for: ${gptQuery}`);

    // then clear input field
    setGptQuery("");
  };

  const toggleDarkMode = () => {
    setIsDarkMode((prevMode) => !prevMode);
  };

  return (
    <View
      style={[
        styles.container,
        {
          backgroundColor: isDarkMode
            ? themeColors.dark.BackgroundColor
            : themeColors.light.BackgroundColor,
        },
      ]}
    >
      <TouchableOpacity style={styles.toggleButton} onPress={toggleDarkMode}>
        <Text>{isDarkMode ? "🌙" : "☀️"}</Text>
      </TouchableOpacity>
      <Text>I like men!</Text>
      {/* <TextInput
        style={styles.input}
        placeholder="enter song name"
        onChangeText={(text) => setSongQuery(text)}
        value={songQuery}
        onSubmitEditing={handleSearch}
      /> */}
      <TextInput
        placeholderTextColor={
          isDarkMode
            ? themeColors.dark.subTitleColor
            : themeColors.light.subTitleColor
        }
        color={
          isDarkMode
            ? themeColors.dark.TextColor1
            : themeColors.light.TextColor3
        }
        onChangeText={(text) => setGptQuery(text)}
        placeholder="Message ChatGpt..."
        value={gptQuery}
        onSubmitEditing={handleGptSearch}
      />
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: themeColors.dark.BackgroundColor,
    alignItems: "center",
    justifyContent: "center",
  },
  toggleButton: {
    position: "absolute",
    top: 50,
    right: 20,
  },
  input: {
    color: themeColors.dark.TextColor1,
  },
});
