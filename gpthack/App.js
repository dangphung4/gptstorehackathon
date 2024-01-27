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
  const [response, setResponse] = useState("");

  const handleSearch = () => {
    console.log(`Searching for music based on: ${songQuery}`);

    setSongQuery("");
  };

  const handleGptSearch = async () => {
    console.log(`Handling GPT search for: ${gptQuery}`);
    try {
      const response = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_id: "userID",
          message: gptQuery,
        }),
      });
      const data = await response.json();
      console.log("API response:", data);
      setResponse(response.reply);
    } catch (error) {
      console.error("Error:", error);
    }
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
      <Text style={styles.text}>{response}</Text>
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
        onSubmitEditing={(event) => {
          event.preventDefault(); // Prevent default behavior
          handleGptSearch(); // Call your custom function
        }}
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
  text: {
    color: themeColors.dark.AccentColor,
  },
});
