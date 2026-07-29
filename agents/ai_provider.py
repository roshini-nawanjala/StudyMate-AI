import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

from config import (
    GROQ_API_KEY,
    OPENROUTER_API_KEY,
    GROQ_MODEL,
    OPENROUTER_MODEL
)

load_dotenv()


class AIProvider:

    TASK_PROVIDER_MAP = {
        "summary": "groq",
        "quiz": "groq",
        "question_answering": "openrouter",
        "reflection": "openrouter",
    }

    def __init__(self):

        self.groq_api_key = GROQ_API_KEY
        self.openrouter_api_key = OPENROUTER_API_KEY

        self.groq_model = GROQ_MODEL
        self.openrouter_model = OPENROUTER_MODEL

    def _groq(self):

        if not self.groq_api_key:
            raise ValueError("Groq API Key not found.")

        return ChatGroq(
            groq_api_key=self.groq_api_key,
            model_name=self.groq_model,
            temperature=0.3,
        )

    def _openrouter(self):

        if not self.openrouter_api_key:
            raise ValueError("OpenRouter API Key not found.")

        return ChatOpenAI(
            api_key=self.openrouter_api_key,
            base_url="https://openrouter.ai/api/v1",
            model=self.openrouter_model,
            temperature=0.3,
        )

    def get_llm(self, provider="auto", task=None):
        """Return an LLM, using task routing only for provider='auto'."""

        provider = provider.lower()

        if provider == "groq":
            return self._groq()

        if provider == "openrouter":
            return self._openrouter()

        if provider == "auto":
            preferred_provider = self.TASK_PROVIDER_MAP.get(task)

            provider_order = [preferred_provider] if preferred_provider else []
            provider_order.extend(
                candidate
                for candidate in ("groq", "openrouter")
                if candidate not in provider_order
            )

            for candidate in provider_order:
                llm = self._try_provider(candidate)
                if llm is not None:
                    return llm

            raise Exception(
                "No valid AI provider found. Please check your API keys."
            )

        raise ValueError(
            "Provider must be: auto, groq or openrouter."
        )

    def _try_provider(self, provider):
        """Try one provider for automatic routing and return None on failure."""
        if provider == "groq" and self.groq_api_key:
            try:
                return self._groq()
            except Exception as e:
                print(f"Groq failed: {e}")

        if provider == "openrouter" and self.openrouter_api_key:
            try:
                return self._openrouter()
            except Exception as e:
                print(f"OpenRouter failed: {e}")

        return None

    def available_providers(self):

        providers = []

        if self.groq_api_key:
            providers.append("Groq")

        if self.openrouter_api_key:
            providers.append("OpenRouter")

        return providers
