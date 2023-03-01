import { StatusBar } from "expo-status-bar";
import React from "react";
import { Text, View } from "react-native";

import { ThemeProvider } from "styled-components";
import { theme } from "./src/infrastracture/theme";

import styled from "styled-components";

const AppContainer = styled(View)`
	flex: 1;
  background-color: ${(props) => props.theme.colors.bg.primary}
	align-items: center;
	justify-content: center;
`;

const WelcomeText = styled(Text)`
	font-size: ${(props) => props.theme.sizes[1]};
	color: blue;
`;

export default function App() {
	return (
		<>
			<ThemeProvider theme={theme}>
				<AppContainer>
					<WelcomeText>You've made it to this side, Say a Yea!!!!!</WelcomeText>
		
		<StatusBar style="auto" />
				</AppContainer>
			</ThemeProvider>
		</>
	);
}
Footer
