from typing import Dict, List, Any

from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.outputs import LLMResult


class AgentCallbackHandler(BaseCallbackHandler):
    def on_llm_start(self, serialized: Dict[str, any], prompts: List[str], **kwargs: Any) -> Any:
        """ Run when the LLM starts running"""
        print(f"***Prompt to LLM was: ***\n{prompts[0]}\n***")
        print("*****")

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> Any:
        """ Run when the LLM finishes running"""
        print(f"***LLM response: ***\n{response.text}\n***")
        print("*****")