/**
 * useAuth Hook - Authentication with native fetch
 */

import { useState, useCallback } from "react"

const API_URL = "http://localhost:8000"

interface AuthState {
  isAuthenticated: boolean
  user: { id: number; email: string } | null
  token: string | null
}

export function useAuth() {
  const [auth, setAuth] = useState<AuthState>({
    isAuthenticated: false,
    user: null,
    token: null,
  })
  const [loading, setLoading] = useState(false)

  const login = useCallback(async (email: string, password: string) => {
    setLoading(true)
    try {
      const response = await fetch(`${API_URL}/api/auth/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      })

      if (!response.ok) throw new Error("Login failed")

      const data = await response.json()
      localStorage.setItem("access_token", data.access_token)

      setAuth({
        isAuthenticated: true,
        user: { id: data.user_id, email },
        token: data.access_token,
      })

      return data
    } catch (err) {
      throw err
    } finally {
      setLoading(false)
    }
  }, [])

  const register = useCallback(async (email: string, username: string, password: string) => {
    setLoading(true)
    try {
      const response = await fetch(`${API_URL}/api/auth/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, username, password }),
      })

      if (!response.ok) throw new Error("Registration failed")

      const data = await response.json()
      return data
    } finally {
      setLoading(false)
    }
  }, [])

  const logout = useCallback(async () => {
    await fetch(`${API_URL}/api/auth/logout`, { method: "POST" })
    localStorage.removeItem("access_token")
    setAuth({ isAuthenticated: false, user: null, token: null })
  }, [])

  const checkAuth = useCallback(async () => {
    const token = localStorage.getItem("access_token")
    if (!token) return

    try {
      const response = await fetch(`${API_URL}/api/auth/me`, {
        headers: { Authorization: `Bearer ${token}` },
      })

      if (response.ok) {
        const user = await response.json()
        setAuth({ isAuthenticated: true, user, token })
      }
    } catch {
      localStorage.removeItem("access_token")
    }
  }, [])

  return { ...auth, loading, login, register, logout, checkAuth }
}
