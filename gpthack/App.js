import { StatusBar } from "expo-status-bar";
import {
  StyleSheet,
  Text,
  View,
  TextInput,
  TouchableOpacity,
} from "react-native";
import React, { useState } from "react";
import { themeColors } from "./ThemeProvider";

const StyledTextInput = ({
  style,
  placeholder,
  value,
  onChangeText,
  ...restProps
}) => (
  <View style={{ position: "relative", width: "100%" }}>
    <TextInput
      style={[
        style,
        {
          textAlign: "center",
          color: themeColors.dark.TextColor1,
        },
      ]}
      placeholder={placeholder}
      value={value}
      onChangeText={onChangeText}
      {...restProps}
    />
    <Text
      style={{
        position: "absolute",
        color: themeColors.dark.subTitleColor,

        textAlign: "center",
        width: "100%",
        opacity: value ? 0 : 1, // Hide placeholder when there is input
      }}
    >
      {placeholder}
    </Text>
  </View>
);

export default function App() {
  const [songQuery, setSongQuery] = useState("");
  const [isDarkMode, setIsDarkMode] = useState(true);
  const [gptQuery, setGptQuery] = useState("");

  const handleSearch = () => {
    // Implement the logic for searching and recommending music based on the songQuery
    // You can make an API call or perform some AI-related operations here
    console.log(`Searching for music based on: ${songQuery}`);
  };

  const handleGptSearch = () => {
    // Implement the logic for handling the GPT search when the input is submitted
    console.log(`Handling GPT search for: ${gptQuery}`);
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
      <StyledTextInput
        //style={styles.input}
        placeholder="Message ChatGPT..."
        onChangeText={(text) => setGptQuery(text)}
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
