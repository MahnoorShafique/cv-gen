# Deployment Guide

This guide shows you how to deploy your CV Generator application using GitHub and various free hosting services.

## Prerequisites

1. **GitHub Account**: Create a free account at [github.com](https://github.com)
2. **Git installed**: Download from [git-scm.com](https://git-scm.com/)

## Step 1: Push Code to GitHub

### Initialize Git Repository (if not already done)
```bash
git init
git add .
git commit -m "Initial commit: CV Generator application"
```

### Create GitHub Repository
1. Go to [github.com](https://github.com) and click "New repository"
2. Name it `cv-generator` (or any name you prefer)
3. Make it public (required for free hosting)
4. Don't initialize with README (since you already have files)
5. Click "Create repository"

### Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/cv-generator.git
git branch -M main
git push -u origin main
```

## Step 2: Choose a Hosting Service

### Option 1: GitHub Pages (Recommended)
**Pros**: Free, automatic deployment, custom domain support
**Cons**: Only static sites, public repos only for free accounts

#### Setup:
1. Go to your repository on GitHub
2. Click "Settings" tab
3. Scroll to "Pages" in the left sidebar
4. Under "Source", select "GitHub Actions"
5. The workflow file (`.github/workflows/deploy.yml`) will automatically deploy your app
6. Your site will be available at: `https://YOUR_USERNAME.github.io/cv-generator/`

#### Custom Domain (Optional):
1. In repository settings > Pages
2. Add your custom domain in "Custom domain" field
3. Create a CNAME file in your repository root with your domain

### Option 2: Netlify
**Pros**: Easy setup, form handling, serverless functions, custom domains
**Cons**: Limited build minutes on free plan

#### Setup:
1. Go to [netlify.com](https://netlify.com) and sign up with GitHub
2. Click "New site from Git"
3. Choose GitHub and select your repository
4. Build settings are automatically detected from `netlify.toml`
5. Click "Deploy site"
6. Your site will be available at a random URL like `https://amazing-name-123456.netlify.app`

#### Custom Domain:
1. In Netlify dashboard > Domain settings
2. Add custom domain
3. Follow DNS configuration instructions

### Option 3: Vercel
**Pros**: Excellent performance, automatic deployments, serverless functions
**Cons**: Limited bandwidth on free plan

#### Setup:
1. Go to [vercel.com](https://vercel.com) and sign up with GitHub
2. Click "New Project"
3. Import your GitHub repository
4. Settings are automatically detected from `vercel.json`
5. Click "Deploy"
6. Your site will be available at `https://cv-generator-YOUR_USERNAME.vercel.app`

### Option 4: Surge.sh
**Pros**: Simple CLI deployment, custom domains
**Cons**: Manual deployment process

#### Setup:
```bash
npm install -g surge
npm run build
cd dist
surge
```

### Option 5: Firebase Hosting
**Pros**: Google infrastructure, good performance, custom domains
**Cons**: Requires Firebase CLI setup

#### Setup:
```bash
npm install -g firebase-tools
firebase login
firebase init hosting
npm run build
firebase deploy
```

## Step 3: Automatic Deployment

### GitHub Actions (Already configured)
- Every push to `main` branch automatically deploys to GitHub Pages
- Check deployment status in "Actions" tab of your repository

### Netlify/Vercel Auto-Deploy
- Both services automatically deploy when you push to GitHub
- No additional configuration needed

## Step 4: Environment Variables (if needed)

If you need environment variables:

### Netlify:
1. Site settings > Environment variables
2. Add variables like `VITE_API_URL`

### Vercel:
1. Project settings > Environment Variables
2. Add variables for different environments

### GitHub Pages:
Environment variables are built into the code during build time.

## Recommended Workflow

1. **Development**: Work locally with `npm run dev`
2. **Testing**: Build locally with `npm run build` and test with `npm run preview`
3. **Deployment**: Push to GitHub, automatic deployment handles the rest

## Custom Domain Setup

### For any hosting service:
1. Buy a domain from providers like Namecheap, GoDaddy, or Cloudflare
2. Configure DNS settings:
   - **GitHub Pages**: Add CNAME record pointing to `YOUR_USERNAME.github.io`
   - **Netlify**: Add CNAME record pointing to your Netlify URL
   - **Vercel**: Add CNAME record pointing to `cname.vercel-dns.com`

## Troubleshooting

### Build Fails:
- Check Node.js version (should be 18+)
- Ensure all dependencies are in `package.json`
- Check build logs for specific errors

### 404 Errors:
- Ensure routing is configured (handled by `netlify.toml` and `vercel.json`)
- For GitHub Pages, make sure base URL is correct in `vite.config.ts`

### Performance Issues:
- Enable gzip compression
- Optimize images
- Use CDN for assets

## Cost Comparison

| Service | Free Tier | Bandwidth | Build Minutes | Custom Domain |
|---------|-----------|-----------|---------------|---------------|
| GitHub Pages | ✅ | 100GB/month | Unlimited | ✅ |
| Netlify | ✅ | 100GB/month | 300 min/month | ✅ |
| Vercel | ✅ | 100GB/month | Unlimited | ✅ |
| Surge.sh | ✅ | 200GB/month | Manual | ✅ |
| Firebase | ✅ | 10GB/month | Unlimited | ✅ |

## Recommendation

**For beginners**: Start with **GitHub Pages** - it's the simplest and most reliable.

**For advanced features**: Use **Netlify** or **Vercel** if you need forms, serverless functions, or better performance.

Your CV Generator is now ready for deployment! 🚀