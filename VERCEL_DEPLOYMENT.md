# Compliment Machine - Vercel Deployment

This is the Vercel-compatible version of the Compliment Machine for **compliments4u.com**

## 🚀 Deploy to Vercel

### Method 1: GitHub (Recommended)

1. **Create a GitHub repository**
   - Go to https://github.com/new
   - Name it: `compliment-machine`
   - Make it Public or Private (your choice)
   - Don't initialize with README (we already have files)

2. **Push your code to GitHub**
   ```bash
   cd /Users/karlkurtz/Documents/compliment-machine
   git init
   git add .
   git commit -m "Initial commit - Vercel version"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/compliment-machine.git
   git push -u origin main
   ```

3. **Deploy to Vercel**
   - Go to https://vercel.com
   - Sign up/login (use GitHub account)
   - Click "Add New Project"
   - Import your `compliment-machine` repository
   - Vercel will auto-detect settings
   - Click "Deploy"
   - Done! You'll get a URL like `compliment-machine.vercel.app`

4. **Connect your domain (compliments4u.com)**
   - In Vercel dashboard, go to your project
   - Click "Settings" → "Domains"
   - Add `compliments4u.com`
   - Vercel will give you nameserver instructions
   - Go to Namecheap and update DNS to Vercel's nameservers
   - Wait 10-60 minutes for DNS to propagate
   - Done! Your site will be live at compliments4u.com

### Method 2: Vercel CLI (Alternative)

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
cd /Users/karlkurtz/Documents/compliment-machine
vercel

# Follow prompts, then connect domain in dashboard
```

## 📁 Project Structure

```
compliment-machine/
├── api/                    # Serverless functions
│   ├── get_compliment.py  # Get random compliment
│   ├── stats.py           # Get statistics
│   ├── guestbook.py       # Get guestbook entries
│   └── guestbook_post.py  # Add guestbook entry
├── public/                # Static files
│   ├── index.html         # Main page
│   ├── guestbook.html     # Guestbook
│   ├── contact.html       # Contact page
│   └── donate.html        # Donation page
├── vercel.json            # Vercel configuration
└── requirements.txt       # Python dependencies
```

## ⚠️ Important Notes

### What Works:
- ✅ Random compliments
- ✅ Guestbook (entries stored temporarily)
- ✅ Statistics counter
- ✅ All pages and navigation
- ✅ Retro 1998 aesthetic

### What Doesn't Work (Yet):
- ❌ LCD display (needs Raspberry Pi)
- ❌ Webcam feed (needs Raspberry Pi)
- ❌ LED indicator (needs Raspberry Pi)

### Limitations:
- Guestbook entries stored in `/tmp` (may reset periodically)
- Stats counter may reset (Vercel serverless is stateless)
- When Raspberry Pi arrives, we'll switch DNS to the Pi version

## 🔄 When Raspberry Pi Arrives

Once your Pi arrives:
1. Keep this Vercel version running
2. Set up Pi with full hardware version
3. Update DNS to point to Pi (or use subdomain like `pi.compliments4u.com`)
4. This Vercel version becomes a backup/mobile version

## 🛠️ Customization

### Update Your Email (contact.html)
Line 221:
```html
<a href="mailto:your-email@example.com?subject=...">
```
Replace `your-email@example.com` with your real email

### Update Your Venmo (donate.html)
Lines 319, 324, 329, 334:
```html
recipients=YOUR-VENMO-USERNAME
```
Replace `YOUR-VENMO-USERNAME` with your Venmo username

### Add More Compliments
Edit `api/get_compliment.py` - add to the `COMPLIMENTS` dictionary

## 📝 Making Updates

After any changes:
```bash
git add .
git commit -m "Description of changes"
git push
```

Vercel will automatically redeploy!

## 🎨 Design

The site uses a authentic 1998 GeoCities aesthetic:
- Comic Sans MS font
- Rainbow animated headers
- Scrolling marquees
- Starry backgrounds
- 3D beveled buttons
- Under construction banners

It's intentionally retro and it's perfect. 🔥

---

**Live Site:** compliments4u.com (once DNS configured)
**Made with ❤️ and a Raspberry Pi (coming soon!)**
