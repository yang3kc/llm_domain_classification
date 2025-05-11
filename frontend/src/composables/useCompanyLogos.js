import OpenAI from '../assets/OpenAI.svg'
import Anthropic from '../assets/Anthropic.svg'
import Google from '../assets/Google.svg'
import Meta from '../assets/Meta.svg'
import DeepSeek from '../assets/DeepSeek.svg'
import XAI from '../assets/XAI.svg'

export const companyLogos = {
  OpenAI,
  Anthropic,
  Google,
  Meta,
  DeepSeek,
  XAI
}

export function useCompanyLogos() {
  const formatCompany = (company) => {
    const logo = companyLogos[company]
    if (logo) {
      return `<img src="${logo}" alt="${company}" class="h-6 inline-block mr-1" /> ${company}`
    }
    return company
  }

  return {
    companyLogos,
    formatCompany
  }
}