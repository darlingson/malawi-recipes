import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Input } from "@/components/ui/input";

export default function Home() {
  return (
      <main className="bg-white">
        {/* Hero Section */}
        <section className="relative bg-gradient-to-b from-red-600 via-white to-green-500 text-center py-20">
          <h1 className="text-5xl font-bold text-black mb-4">Malawian Recipes</h1>
          <p className="text-lg text-gray-700 max-w-3xl mx-auto">
            Dive into the heart of Malawian cuisine. Explore traditional recipes, learn cooking tips, and embrace the flavors of Malawi.
          </p>
          <Button className="mt-8 bg-green-600 hover:bg-green-700 text-white">Explore Recipes</Button>
        </section>

        {/* Features Section */}
        <section className="py-16 px-6 bg-gray-50">
          <div className="max-w-6xl mx-auto">
            <h2 className="text-3xl font-bold text-black text-center mb-8">Why Choose Malawian Recipes?</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              <FeatureCard
                  title="Authentic Flavors"
                  description="Experience recipes passed down through generations."
                  icon="🥘"
              />
              <FeatureCard
                  title="Easy to Follow"
                  description="Step-by-step instructions for cooks of all levels."
                  icon="📖"
              />
              <FeatureCard
                  title="Community Driven"
                  description="Share and discover recipes from fellow food enthusiasts."
                  icon="🌍"
              />
            </div>
          </div>
        </section>

        {/* Popular Recipes Section */}
        <section className="py-16 px-6 bg-white">
          <div className="max-w-6xl mx-auto">
            <h2 className="text-3xl font-bold text-black text-center mb-8">Popular Recipes</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              {["Nsima & Ndiwo", "Chambo Fish", "Mandasi"].map((recipe, idx) => (
                  <RecipeCard key={idx} title={recipe} />
              ))}
            </div>
          </div>
        </section>

        {/* About Section */}
        <section className="py-16 px-6 bg-red-50">
          <div className="max-w-4xl mx-auto text-center">
            <h2 className="text-3xl font-bold text-black mb-4">About Malawian Cuisine</h2>
            <p className="text-lg text-gray-700">
              Malawian cuisine is a celebration of natural ingredients, traditional cooking methods, and rich cultural heritage. From the staple nsima to the flavorful chambo fish, every dish tells a story.
            </p>
          </div>
        </section>

        {/* Newsletter Section */}
        <section className="py-16 px-6 bg-green-500 text-white text-center">
          <h2 className="text-3xl font-bold mb-4">Stay Updated!</h2>
          <p className="mb-8">Sign up for our newsletter to get the latest recipes and updates straight to your inbox.</p>
          <form className="flex flex-col sm:flex-row justify-center gap-4 max-w-lg mx-auto">
            <Input
                type="email"
                placeholder="Enter your email"
                className="px-4 py-2 rounded-md border-none focus:outline-none text-black"
            />
            <Button className="bg-red-600 px-6 py-2 rounded-md hover:bg-red-700">Subscribe</Button>
          </form>
        </section>

        {/* Footer */}
        <footer className="bg-black text-white py-8">
          <div className="max-w-6xl mx-auto text-center">
            <p>© 2024 Malawian Recipes. All rights reserved.</p>
            <div className="flex justify-center gap-4 mt-4">
              <a href="#" className="hover:text-red-600">Privacy Policy</a>
              <a href="#" className="hover:text-red-600">Terms of Service</a>
              <a href="#" className="hover:text-red-600">Contact Us</a>
            </div>
          </div>
        </footer>
      </main>
  );
}

const FeatureCard = ({ title, description, icon }: { title: string; description: string; icon: string }) => (
    <Card className="bg-white rounded-lg shadow-lg p-6 text-center">
      <CardHeader>
        <div className="text-4xl">{icon}</div>
        <CardTitle className="text-xl font-bold text-black mt-4">{title}</CardTitle>
        <CardDescription className="text-gray-600 mt-2">{description}</CardDescription>
      </CardHeader>
    </Card>
);

const RecipeCard = ({ title }: { title: string }) => (
    <Card className="bg-gray-100 rounded-lg shadow-lg overflow-hidden">
      <div className="h-40 bg-cover bg-center" style={{ backgroundImage: "url('/placeholder.jpg')" }}></div>
      <CardContent className="p-4">
        <CardTitle className="text-lg font-bold text-black">{title}</CardTitle>
        <CardDescription className="text-gray-600">Delicious and easy-to-make.</CardDescription>
      </CardContent>
    </Card>
);
