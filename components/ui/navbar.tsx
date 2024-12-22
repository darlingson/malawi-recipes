import Link from "next/link";

export const Navbar = () => {
    return (
        <nav className="bg-black text-white py-4 shadow-md">
            <div className="flex items-center pl-4">
                <Link href="/" className="text-2xl font-bold text-white">
                    Malawian Recipes
                </Link>
            </div>
        </nav>
    );
};
