import type { Metadata } from "next";
import { Geist, Geist_Mono, Alfa_Slab_One, Baloo_Chettan_2, Quicksand, Righteous } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
	variable: "--font-geist-sans",
	subsets: ["latin"],
});

const geistMono = Geist_Mono({
	variable: "--font-geist-mono",
	subsets: ["latin"],
});

const alfaSlabOne = Alfa_Slab_One({
	variable: "--font-alfa-slab-one",
	subsets: ["latin"],
	weight: "400",
});

const balooChettan2 = Baloo_Chettan_2({
	variable: "--font-baloo-chettan-2",
	subsets: ["latin"],
});

const quicksand = Quicksand({
	variable: "--font-quicksand",
	subsets: ["latin"],
});

const righteous = Righteous({
	variable: "--font-righteous",
	subsets: ["latin"],
	weight: "400",
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
			className={`${geistSans.variable} ${geistMono.variable} ${alfaSlabOne.variable} ${balooChettan2.variable} ${quicksand.variable} ${righteous.variable} h-full antialiased`}
			suppressHydrationWarning
		>
			<body className="min-h-full flex flex-col" suppressHydrationWarning>
				{children}
			</body>
		</html>
	);
}
