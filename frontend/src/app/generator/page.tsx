"use client";

import { Button } from "@/components/ui/button";
import Upload from "@/utils/Uploader";
import { useEffect, useState } from "react";

interface IDataModel {
  id: number;
  body: string;
  title: string;
}

export default function Generator() {
  const [output, setOutput] = useState("Loading...");
  const [data, setData] = useState<IDataModel[]>([]);
  const [url, setUrl] = useState("");
  const [file, setFile] = useState<File | null>(null);

  useEffect(() => {
    const genmd = async () => {
      try {
        const response = await fetch("https://localhost:3000/api", {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        });

        const json = (await response.json()) as IDataModel[];
        if (response.ok) {
          setData(json);
        } else {
          setOutput("Failed to fetch data");
        }
      } catch (err) {
        console.error("Error fetching data:", err);
        setOutput("Error fetching data");
      }
    };

    genmd();
  }, []);

  const handlesubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (url) {
      console.log("url", url);
    } else if (file) {
      console.log("file", file);
    }

    if (!url && !file) {
      console.log("no url or file");
    }
  };

  return (
    <div className="flex justify-between p-10 bg-slate-100 w-full h-full space-x-10">
      <div className="bg-white p-10 rounded-lg w-1/2 shadow-lg">
        <form className="space-y-4" onSubmit={handlesubmit}>
          <div>
            <label className="block">Github Repo URL</label>
            <input
              type="text"
              placeholder="https://github.com/user/repo"
              className="border w-md p-2 rounded"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
            />
            <div className="flex items-center my-2">
              <div className="h-[1px] bg-gradient-to-r from-transparent to-gray-300 flex-grow"></div>
              <div className="mx-2 text-muted-foreground">OR</div>
              <div className="h-[1px] bg-gradient-to-l from-transparent to-gray-300 flex-grow"></div>
            </div>
            <Upload onFileSelect={(file) => setFile(file)} />
          </div>
          <Button className="w-full">Submit</Button>
        </form>
      </div>
      <div className="bg-white p-10 rounded-lg w-1/2 shadow-lg">
        <div className="border-2 border-slate-100 h-full rounded-lg">
          <div className="text-muted-foreground p-4">{output}</div>
        </div>
      </div>
    </div>
  );
}
