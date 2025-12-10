/**
 * Auth API - Authentication endpoints
 */

import { apiClient } from "./client"

export interface LoginRequest {
  email: string
  password: string
}

export interface RegisterRequest {
  email: string
  username: string
  password: string
}

export interface AuthResponse {
  access_token: string
  token_type: string
  user_id: number
}

export async function login(credentials: LoginRequest): Promise<AuthResponse> {
  const response = await apiClient.post("/api/auth/login", credentials)
  return response.data
}

export async function register(data: RegisterRequest): Promise<AuthResponse> {
  const response = await apiClient.post("/api/auth/register", data)
  return response.data
}

export async function logout(): Promise<void> {
  await apiClient.post("/api/auth/logout")
  localStorage.removeItem("access_token")
}

export async function getCurrentUser() {
  const response = await apiClient.get("/api/auth/me")
  return response.data
}
