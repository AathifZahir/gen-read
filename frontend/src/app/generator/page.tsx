import { Button } from "@/components/ui/button";
import Upload from "@/utils/Uploader";

export default function generator() {
  return (
    <div className="flex justify-between p-10 bg-slate-100 w-full h-full space-x-10">
      <div className="bg-white p-10 rounded-lg w-1/2 shadow-lg">
        <form className="space-y-4">
          <div>
            <label className="block">Github Repo URL</label>
            <input
              type="text"
              placeholder="https://github.com/user/repo"
              className="border w-md p-2 rounded"
            />
            <div className="flex items-center my-2">
              <div className="h-[1px] bg-gradient-to-r from-transparent to-gray-300 flex-grow"></div>
              <div className="mx-2 text-muted-foreground">OR</div>
              <div className="h-[1px] bg-gradient-to-l from-transparent to-gray-300 flex-grow"></div>
            </div>
            <Upload />
          </div>
          <Button className="w-full">Submit</Button>
        </form>
      </div>
      <div className="bg-white p-10 rounded-lg w-1/2 shadow-lg">
        <div className="border-2 border-slate-100 h-full rounded-lg">
          <div className="text-muted-foreground p-4">output here...</div>
        </div>
      </div>
    </div>
  );
}
