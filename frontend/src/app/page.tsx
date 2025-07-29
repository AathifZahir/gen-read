"use client";

import { Button } from "@/components/ui/button";
import generator from "./generator/page";
import { useRouter } from "next/navigation";

export default function Home() {
  const router = useRouter();
  function handleStart() {
    router.push("/generator");
  }
  return (
    <div className="h-full flex items-center justify-center">
      <div className="text-center m-20 space-y-10">
        <div className="font-bitcount text-3xl">
          Generate Professional READMEs
        </div>
        <div className="mx-50 font-playfair text-xl">
          Transform your GitHub repositories and ZIP files into perfectly
          structured and informative README.md files in seconds. Focus on
          coding, let AI handle the documentation.
        </div>
        <Button onClick={handleStart}>Get Started</Button>
      </div>
    </div>
  );
}
