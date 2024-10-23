

import { getSortedPostsData } from '../lib/recipes';

// Async server component for App Router
export default async function Home() {
  // Fetch the post data
  const allPostsData = await getSortedPostsData();

  return (
    <ul>
      {allPostsData.map(({ id, date, title }) => (
        <li key={id}>
          <strong>{title}</strong>
          <br />
          <span>{id}</span>
          <br />
          <span>{date}</span>
        </li>
      ))}
    </ul>
  );
}
