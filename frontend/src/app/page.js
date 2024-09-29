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
