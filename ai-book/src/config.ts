/**
 * Application configuration
 * Reads API URL from Docusaurus customFields
 */

import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

export const useConfig = () => {
  const { siteConfig } = useDocusaurusContext();
  const apiUrl = (siteConfig.customFields?.apiUrl as string) || 'http://localhost:8000';

  return {
    apiUrl,
    chatEndpoint: `${apiUrl}/api/chat`,
  };
};
