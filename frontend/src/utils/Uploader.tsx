"use client";

import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { useCallback, useState } from "react";
import { useDropzone } from "react-dropzone";
import { FileArchive } from "lucide-react";

interface UploadProps {
  onFileSelect: (file: File) => void;
}

export default function Upload({ onFileSelect }: UploadProps) {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const onDrop = useCallback(
    (acceptedFiles: File[]) => {
      console.log(acceptedFiles);
      if (acceptedFiles.length > 0) {
        const zipFile = acceptedFiles[0];
        if (
          zipFile.type === "application/zip" ||
          zipFile.name.endsWith(".zip")
        ) {
          setSelectedFile(zipFile);
          onFileSelect(zipFile);
        } else {
          alert("Please select a zip file");
        }
      }
    },
    [onFileSelect]
  );

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: { "application/zip": [".zip"] },
    multiple: false,
    maxFiles: 1,
  });

  const removeFile = () => {
    setSelectedFile(null);
    onFileSelect(null as unknown as File);
  };

  return (
    <div>
      <div
        {...getRootProps()}
        className={cn(
          "border-dashed border-2 border-border rounded-lg h-64 flex items-center justify-center transition ease-in-out duration-300",
          isDragActive && "border-ring"
        )}
      >
        <input {...getInputProps()} />
        {isDragActive ? (
          <div className="flex flex-col items-center justify-center">
            <p className="text-center font-medium mb-1">
              Drag & drop some files here
            </p>
            <p className="text-muted-foreground font-regular text-xs mb-6">
              or click to browse(.zip only)
            </p>
            <Button type="button">Select File</Button>
          </div>
        ) : (
          <div className="flex flex-col items-center justify-center">
            <p className="text-center font-medium mb-1">
              Drag & drop some files here
            </p>
            <p className="text-muted-foreground font-regular text-xs mb-6">
              or click to browse(.zip only)
            </p>
            <Button variant={"outline"} type="button">
              Select File
            </Button>
          </div>
        )}
      </div>
      <div>
        {selectedFile ? (
          <div className="border-dashed border-2 border-border rounded-lg py-2 mt-2 flex items-center justify-between px-4 transition ease-in-out duration-300">
            <div className="flex flex items-center justify-center space-x-2">
              <FileArchive size={32} />
              <div className="text-sm">
                <div>{selectedFile?.name}</div>
                <div>{(selectedFile.size / (1024 * 1024)).toFixed(2)} MB</div>
              </div>
            </div>
            <div className="text-bold">
              <Button
                variant="ghost"
                size="sm"
                onClick={(e) => {
                  e.preventDefault();
                  removeFile();
                }}
              >
                X
              </Button>
            </div>
          </div>
        ) : (
          <div></div>
        )}
      </div>
    </div>
  );
}
