/**
 * usePosts Hook - Post management with fetch API
 */

import { useState, useCallback } from "react"

const API_URL = "http://localhost:8000"

export interface Post {
  id: number
  title: string
  content: string
  user_id: number
}

export function usePosts() {
  const [posts, setPosts] = useState<Post[]>([])
  const [loading, setLoading] = useState(false)

  const fetchPosts = useCallback(async () => {
    setLoading(true)
    try {
      const response = await fetch(`${API_URL}/api/posts`)
      const data = await response.json()
      setPosts(data)
    } finally {
      setLoading(false)
    }
  }, [])

  const fetchPostsByUser = useCallback(async (userId: number) => {
    setLoading(true)
    try {
      const response = await fetch(`${API_URL}/api/posts/user/${userId}`)
      const data = await response.json()
      return data
    } finally {
      setLoading(false)
    }
  }, [])

  const createPost = useCallback(async (title: string, content: string, userId: number) => {
    const response = await fetch(`${API_URL}/api/posts`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, content, user_id: userId }),
    })
    const newPost = await response.json()
    setPosts((prev) => [newPost, ...prev])
    return newPost
  }, [])

  const updatePost = useCallback(async (postId: number, data: { title?: string; content?: string }) => {
    const response = await fetch(`${API_URL}/api/posts/${postId}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    })
    const updated = await response.json()
    setPosts((prev) => prev.map((p) => (p.id === postId ? updated : p)))
    return updated
  }, [])

  const deletePost = useCallback(async (postId: number) => {
    await fetch(`${API_URL}/api/posts/${postId}`, { method: "DELETE" })
    setPosts((prev) => prev.filter((p) => p.id !== postId))
  }, [])

  return { posts, loading, fetchPosts, fetchPostsByUser, createPost, updatePost, deletePost }
}
