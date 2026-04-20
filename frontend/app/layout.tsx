import type { Metadata } from "next";
import { Geist, Geist_Mono, Quicksand } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
	variable: "--font-geist-sans",
	subsets: ["latin"],
});

const geistMono = Geist_Mono({
	variable: "--font-geist-mono",
	subsets: ["latin"],
});

const quicksand = Quicksand({
	variable: "--font-quicksand",
	subsets: ["latin"],
});

export const metadata: Metadata = {
	title: "El Clasico",
	description: "El Clasico | Štatistiky, program a zápasy medzi FC Barcelona a Real Madrid",
};

export default function RootLayout({
	children,
}: Readonly<{
	children: React.ReactNode;
}>) {
	return (
		<html
			lang="en"
			className={`${geistSans.variable} ${geistMono.variable} ${quicksand.variable} h-full antialiased`}
			suppressHydrationWarning
		>
			<body className="min-h-full flex flex-col" suppressHydrationWarning>
				{children}
			</body>
		</html>
	);
}
