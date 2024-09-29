'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'

export default function Home() {
  const [city, setCity] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const router = useRouter()

  const handleSubmit = async (e) => {
    e.preventDefault()
    setIsLoading(true)
    // In a real application, you would send this data to your backend
    // and update the JupyterLite notebook with the new city data
    await new Promise(resolve => setTimeout(resolve, 1000)) // Simulating API call
    router.push(`/?city=${encodeURIComponent(city)}`)
    setIsLoading(false)
  }

  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-2">
      <h2 className="text-5xl font-bold mb-8 futuristic-text glow">Welcome to Mold Your City</h2>
      <p className="text-xl mb-8 text-center max-w-2xl text-blue-200">
        Enter a city name to see how slime mold simulations can help plan the ideal subway routes.
      </p>
      <form onSubmit={handleSubmit} className="w-full max-w-md">
        <div className="flex items-center border-b border-blue-500 py-2 glow-input">
          <input
            className="appearance-none bg-transparent border-none w-full text-white mr-3 py-1 px-2 leading-tight focus:outline-none placeholder-blue-300"
            type="text"
            placeholder="Enter city name"
            aria-label="City name"
            value={city}
            onChange={(e) => setCity(e.target.value)}
            required
          />
          <button
            className="flex-shrink-0 bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded-full transition duration-300 ease-in-out transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-50"
            type="submit"
            disabled={isLoading}
          >
            {isLoading ? 'Simulating...' : 'Simulate'}
          </button>
        </div>
      </form>
      <div className="mt-8 w-full max-w-4xl">
        <div className="iframe-container">
          <iframe
            src="https://victoria-dr.github.io/mold-your-city-simulation/lab/index.html"
            width="100%"
            height="600px"
            style={{border: 'none'}}
          ></iframe>
        </div>
      </div>
    </div>
  )
}
