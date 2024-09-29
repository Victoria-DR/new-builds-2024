import { Inter } from 'next/font/google'
import './globals.css'
import './custom.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'Mold Your City',
  description: 'Urban planning tool using slime mold simulations for subway route planning',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={`${inter.className} bg-gradient-to-br from-slate-900 to-blue-900 text-white min-h-screen`}>
        <div className="organic-blob"></div>
        <header className="bg-transparent text-white p-6">
          <h1 className="text-4xl font-bold futuristic-text">Mold Your City</h1>
        </header>
        <main className="container mx-auto p-4 relative z-10">
          {children}
        </main>
        <footer className="bg-transparent p-4 text-center text-blue-300">
          <p>&copy; 2024 Mold Your City. All rights reserved.</p>
        </footer>
      </body>
    </html>
  )
}
