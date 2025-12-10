/**
 * Posts API - Post management endpoints
 */

import { apiClient } from "./client"

export interface Post {
  id: number
  title: string
  content: string
  user_id: number
}

export interface CreatePostRequest {
  title: string
  content: string
  user_id: number
}

export interface UpdatePostRequest {
  title?: string
  content?: string
}

export async function getPosts(): Promise<Post[]> {
  const response = await apiClient.get("/api/posts")
  return response.data
}

export async function getPostById(postId: number): Promise<Post> {
  const response = await apiClient.get(`/api/posts/${postId}`)
  return response.data
}

export async function getPostsByUser(userId: number): Promise<Post[]> {
  const response = await apiClient.get(`/api/posts/user/${userId}`)
  return response.data
}

export async function createPost(data: CreatePostRequest): Promise<Post> {
  const response = await apiClient.post("/api/posts", data)
  return response.data
}

export async function updatePost(postId: number, data: UpdatePostRequest): Promise<Post> {
  const response = await apiClient.put(`/api/posts/${postId}`, data)
  return response.data
}

export async function deletePost(postId: number): Promise<void> {
  await apiClient.delete(`/api/posts/${postId}`)
}
