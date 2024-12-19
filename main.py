import subprocess
import os
import sys

def run_command(command, prompt=None):
    """Menjalankan perintah shell dan menangani error."""
    if prompt:
        print(f"\n{prompt}")
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError:
        sys.exit("❌ Command failed. Exiting...")

def create_nextjs_project(project_name):
    """Membuat proyek Next.js dengan TypeScript dan ESLint."""
    command = f"npx create-next-app@latest {project_name} --typescript --eslint"
    run_command(command, f"🚀 Creating Next.js project '{project_name}' with TypeScript and ESLint...")

def install_tailwindcss():
    """Menginstal Tailwind CSS dan dependensi lainnya."""
    print("\n📦 Installing Tailwind CSS and related dependencies...")
    run_command("npm install -D tailwindcss postcss autoprefixer")
    run_command("npx tailwindcss init -p")

def configure_tailwind():
    """Mengonfigurasi file tailwind.config.js untuk mendukung dark mode."""
    print("\n🛠️ Configuring Tailwind CSS with dark mode support...")
    config_content = """/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",

    "./src/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
"""
    with open("tailwind.config.js", "w") as f:
        f.write(config_content)
    print("✅ Tailwind CSS configuration updated with dark mode support.")

def update_globals_css():
    """Menambahkan direktif Tailwind CSS dan gaya dasar ke globals.css dengan dukungan dark mode."""
    print("\n🎨 Adding Tailwind CSS directives to globals.css with dark mode support...")
    globals_css_path = os.path.join("src", "app", "globals.css")
    with open(globals_css_path, "w") as f:
        f.write("""@tailwind base;
@tailwind components;
@tailwind utilities;

/* Dark mode support */
body {
  @apply bg-gray-100 text-gray-800 transition-colors duration-300;
}

body.dark {
  @apply bg-gray-900 text-gray-100;
}
""")
    print("✅ globals.css updated with Tailwind directives and dark mode support.")

def update_page_tsx():
    """Mengganti konten default di src/app/page.tsx dengan contoh desain responsif dan dark mode toggle."""
    print("\n📝 Updating src/app/page.tsx with responsive design and dark mode toggle...")
    page_path = os.path.join("src", "app", "page.tsx")
    with open(page_path, "w") as f:
        f.write("""\"use client\";
import { useState, useEffect } from 'react';

export default function Home() {
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);

  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-4 bg-gray-100 dark:bg-gray-900 text-gray-800 dark:text-gray-100 transition-colors duration-300">
      <h1 className="text-4xl font-bold mb-4">
        Welcome to Next.js with Tailwind CSS!
      </h1>
      <p className="mb-6 text-lg text-center max-w-md">
        This is an example of a responsive design with a dark mode switcher.
      </p>
      <button
        onClick={() => setDarkMode(!darkMode)}
        className="px-6 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 dark:bg-blue-700 dark:hover:bg-blue-600 transition"
      >
        Toggle {darkMode ? 'Light' : 'Dark'} Mode
      </button>
    </main>
  );
}
""")
    print("✅ src/app/page.tsx updated with responsive design and dark mode toggle.")

def main():
    """Fungsi utama untuk mengatur proyek Next.js dengan Tailwind CSS dan dark mode."""
    print("=== 🚀 Next.js + Tailwind CSS with Dark Mode Setup Automation 🚀 ===\n")

    project_name = input("Enter your Next.js project name: ").strip()
    if not project_name:
        sys.exit("❌ Project name cannot be empty.")

    # Cek apakah direktori sudah ada
    if os.path.exists(project_name):
        sys.exit(f"❌ Project '{project_name}' already exists. Please choose a different name.")

    # Membuat proyek Next.js
    create_nextjs_project(project_name)

    # Berpindah ke direktori proyek
    os.chdir(project_name)

    # Menginstal Tailwind CSS
    install_tailwindcss()

    # Mengonfigurasi Tailwind CSS dengan dark mode
    configure_tailwind()

    # Memperbarui globals.css dengan direktif Tailwind dan gaya dasar
    update_globals_css()

    # Memperbarui halaman page.tsx dengan contoh desain responsif dan dark mode toggle
    update_page_tsx()

    print("\n🎉 Your Next.js project with Tailwind CSS and dark mode is ready!")
    print(f"\n➡️ To get started, run:\n  cd {project_name}\n  npm run dev\n")

if __name__ == "__main__":
    main()
