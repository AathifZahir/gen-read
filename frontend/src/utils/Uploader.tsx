"use client";

import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { useCallback } from "react";
import { useDropzone } from "react-dropzone";

export default function Upload() {
  const onDrop = useCallback((acceptedFiles: File[]) => {
    // Do something with the files
    console.log(acceptedFiles);
  }, []);
  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

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
          <Button>Select File</Button>
        </div>
      ) : (
        <div className="flex flex-col items-center justify-center">
          <p className="text-center font-medium mb-1">
            Drag & drop some files here
          </p>
          <p className="text-muted-foreground font-regular text-xs mb-6">
            or click to browse(.zip only)
          </p>
          <Button variant={"outline"}>Select File</Button>
        </div>
      )}
    </div>
  );
}
