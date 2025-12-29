/**
 * Application configuration
 * Environment variables for Docusaurus must be prefixed with DOCUSAURUS_
 */

// API URL configuration - defaults to localhost for development
export const API_URL =
  typeof window !== 'undefined' && (window as any).DOCUSAURUS_API_URL
    ? (window as any).DOCUSAURUS_API_URL
    : process.env.DOCUSAURUS_API_URL || 'http://localhost:8000';

export const config = {
  apiUrl: API_URL,
  chatEndpoint: `${API_URL}/api/chat`,
};
