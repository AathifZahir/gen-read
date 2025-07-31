import type { Metadata } from "next";
import {
  Inter,
  Bitcount_Grid_Double,
  Playfair_Display,
  Geist,
} from "next/font/google";
import "./globals.css";
import Header from "@/components/header";
import Footer from "@/components/footer";

const inter = Inter({
  subsets: ["latin"],
});

const giest = Geist({
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
    <html lang="en" className="h-full">
      <body className={`${giest.className} antialiased h-full flex flex-col`}>
        <Header />
        <main className="flex-1">{children}</main>
        <Footer />
      </body>
    </html>
  );
}
