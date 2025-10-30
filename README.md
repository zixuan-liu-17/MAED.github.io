
Website for MAED

## Editing without coding (Decap CMS)

This site includes a no-code editor at `/admin/` powered by Decap CMS. It lets editors update pages, posts, and data files in the repository via a friendly UI.

### One-time setup (maintainer)
1. Create a Netlify site connected to this GitHub repo (Use the default build settings; we still host on GitHub Pages).
2. In Netlify → Identity: Enable Identity.
3. In Identity → Settings → Services: Enable Git Gateway.
4. Invite editors via Identity → Invite users. They will accept via email and can sign in.

Note: Hosting remains on GitHub Pages. Netlify is only used for authentication and Git Gateway.

### How editors log in
1. Visit `https://zixuan-liu-17.github.io/MAED.github.io/admin/`.
2. Click “Login” (Netlify Identity modal).
3. After login, you can edit:
   - Posts (`_posts`)
   - Pages (About, Application, Dataset, Get Involved, Learning Capacity, Coming Soon, Editing Guide)
   - Data files (`_data/*.yml`)
4. Changes are committed to the `main` branch via pull requests (editorial workflow). Publish when ready.

### Media uploads
- Uploaded images are stored in `assets/img` and referenced as `/assets/img/...`.

### Admin config
- See `admin/config.yml` for collections and fields. Update as site structure evolves.
