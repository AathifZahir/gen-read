import {
  NavigationMenu,
  NavigationMenuLink,
  NavigationMenuItem,
  NavigationMenuList,
} from "@/components/ui/navigation-menu";

export default function footer() {
  return (
    <footer className="border-t mt-10 py-6 text-center text-sm text-muted-foreground">
      <p>
        © {new Date().getFullYear()} GenRead. Built with ❤️ by{" "}
        <a
          href="https://az-dev.vercel.app/"
          target="_blank"
          rel="noopener noreferrer"
          className="underline hover:text-foreground"
        >
          Aathif Zahir
        </a>
        .
      </p>
    </footer>
  );
}
