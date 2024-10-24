import fs from "fs";
import path from "path";
import matter from "gray-matter";

interface PostData {
  id: string;
  title?: string; // Add other fields as needed
  date: string; // Assuming date is a string (ISO format or similar)
}
const postsDirectory = path.join(process.cwd(), "posts");

export async function getSortedPostsData(): Promise<PostData[]> {
  // Get file names under /posts
  const fileNames = fs.readdirSync(postsDirectory);
  const allPostsData = fileNames.map((fileName) => {
    // Remove ".md" from file name to get id
    const id = fileName.replace(/\.md$/, "");

    // Read markdown file as string
    const fullPath = path.join(postsDirectory, fileName);
    const fileContents = fs.readFileSync(fullPath, "utf8");

    // Use gray-matter to parse the post metadata section
    const matterResult = matter(fileContents);

    // Combine the data with the id
    const postData = {
      id,
      ...(matterResult.data as Omit<PostData, "id">), // Type assertion
    };
    // return {
    //   id,
    //   ...matterResult.data,
    // };
    return postData;
  });
  // Sort posts by date
  return allPostsData.sort(({ date: a }, { date: b }) => {
    if (a < b) {
      return 1;
    } else if (a > b) {
      return -1;
    } else {
      return 0;
    }
  });
}
