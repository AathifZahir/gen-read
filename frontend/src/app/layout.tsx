import type { Metadata } from "next";
import {
  Inter,
  Bitcount_Grid_Double,
  Playfair_Display,
} from "next/font/google";
import "./globals.css";
import Header from "@/components/header";

const inter = Inter({
  subsets: ["latin"],
});

const bitcount = Bitcount_Grid_Double({
  subsets: ["latin"],
});

const playfair = Playfair_Display({
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "GenRead",
  description: "AI readme generator",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${inter.className} antialiased`}>
        <Header />
        {children}
      </body>
    </html>
  );
}
