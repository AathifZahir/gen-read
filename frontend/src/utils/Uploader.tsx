"use client";

import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { useCallback } from "react";
import { useDropzone } from "react-dropzone";

interface UploadProps {
  onFileSelect: (file: File) => void;
}

export default function Upload({ onFileSelect }: UploadProps) {
  const onDrop = useCallback(
    (acceptedFiles: File[]) => {
      console.log(acceptedFiles);
      if (acceptedFiles.length > 0) {
        const zipFile = acceptedFiles[0];
        if (
          zipFile.type === "application/zip" ||
          zipFile.name.endsWith(".zip")
        ) {
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

  return (
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
  );
}
