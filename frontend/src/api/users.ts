/**
 * Users API - User management endpoints
 */

import { apiClient } from "./client"

export interface User {
  id: number
  email: string
  username: string
}

export interface CreateUserRequest {
  email: string
  username: string
  password: string
}

export interface UpdateUserRequest {
  email?: string
  username?: string
}

export async function getUsers(): Promise<User[]> {
  const response = await apiClient.get("/api/users")
  return response.data
}

export async function getUserById(userId: number): Promise<User> {
  const response = await apiClient.get(`/api/users/${userId}`)
  return response.data
}

export async function createUser(data: CreateUserRequest): Promise<User> {
  const response = await apiClient.post("/api/users", data)
  return response.data
}

export async function updateUser(userId: number, data: UpdateUserRequest): Promise<User> {
  const response = await apiClient.put(`/api/users/${userId}`, data)
  return response.data
}

export async function deleteUser(userId: number): Promise<void> {
  await apiClient.delete(`/api/users/${userId}`)
}
