import { Button } from "@/components/ui/button";

export default function Home() {
  return (
    <div>
      <div className="text-center m-10 space-y-10">
        <div className="font-bitcount text-3xl">
          Generate Professional READMEs
        </div>
        <div className="mx-50 font-playfair text-xl">
          Transform your GitHub repositories and ZIP files into perfectly
          structured and informative README.md files in seconds. Focus on
          coding, let AI handle the documentation.
        </div>
        <Button>Get Started</Button>
      </div>
    </div>
  );
}
