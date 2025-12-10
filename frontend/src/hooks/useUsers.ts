/**
 * useUsers Hook - Fetch users using native fetch API
 */

import { useState, useEffect, useCallback } from "react"

const API_URL = "http://localhost:8000"

export interface User {
  id: number
  email: string
  username: string
}

export function useUsers() {
  const [users, setUsers] = useState<User[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const fetchUsers = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const response = await fetch(`${API_URL}/api/users`)
      if (!response.ok) throw new Error("Failed to fetch users")
      const data = await response.json()
      setUsers(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : "Unknown error")
    } finally {
      setLoading(false)
    }
  }, [])

  const createUser = useCallback(async (userData: { email: string; username: string; password: string }) => {
    setLoading(true)
    try {
      const response = await fetch(`${API_URL}/api/users`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(userData),
      })
      if (!response.ok) throw new Error("Failed to create user")
      const newUser = await response.json()
      setUsers((prev) => [...prev, newUser])
      return newUser
    } catch (err) {
      setError(err instanceof Error ? err.message : "Unknown error")
      throw err
    } finally {
      setLoading(false)
    }
  }, [])

  const deleteUser = useCallback(async (userId: number) => {
    try {
      const response = await fetch(`${API_URL}/api/users/${userId}`, {
        method: "DELETE",
      })
      if (!response.ok) throw new Error("Failed to delete user")
      setUsers((prev) => prev.filter((u) => u.id !== userId))
    } catch (err) {
      setError(err instanceof Error ? err.message : "Unknown error")
      throw err
    }
  }, [])

  useEffect(() => {
    fetchUsers()
  }, [fetchUsers])

  return { users, loading, error, fetchUsers, createUser, deleteUser }
}
