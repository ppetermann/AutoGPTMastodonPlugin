"""This is a template for Auto-GPT plugins."""
import abc
from typing import Any, Dict, List, Optional, Tuple, TypeVar, TypedDict
from auto_gpt_plugin_template import AutoGPTPluginTemplate
from .mastodon_plugin.check_env import check_env

PromptGenerator = TypeVar("PromptGenerator")


class Message(TypedDict):
    role: str
    content: str


class AutoGPTMastodonPlugin(AutoGPTPluginTemplate):
    """
    This is a simple plugin to provide the ability to pst to a mastodon instance
    """

    def __init__(self):
        super().__init__()
        self._name = "Auto-GPT-Mastodon-Plugin"
        self._version = "0.1.0"
        self._description = "A simple plugin to provide the capability to post to Mastodon"

    def can_handle_on_response(self) -> bool:
        return False

    def on_response(self, response: str, *args, **kwargs) -> str:
        pass

    def can_handle_post_prompt(self) -> bool:
        return True

    def post_prompt(self, prompt: PromptGenerator) -> PromptGenerator:
        from .mastodon_plugin.mastodon_plugin import (
            send_toot,
            check_mastodon_notifications
        )

        if not check_env():
            return prompt

        prompt.add_command(
            "Send Toot",
            "send_toot",
            {"content": "<content>"},
            send_toot,
        )

        prompt.add_command(
            "Check Mastodon Notifications",
            "check_mastodon_notifications",
            {},
            check_mastodon_notifications
        )

        return prompt

    def can_handle_on_planning(self) -> bool:
        return False

    def on_planning(
            self, prompt: PromptGenerator, messages: List[Message]
    ) -> Optional[str]:
        pass

    def can_handle_post_planning(self) -> bool:
        return False
    def post_planning(self, response: str) -> str:
        pass

    def can_handle_pre_instruction(self) -> bool:
        return False

    def pre_instruction(self, messages: List[Message]) -> List[Message]:
        pass

    def can_handle_on_instruction(self) -> bool:
        return False

    def on_instruction(self, messages: List[Message]) -> Optional[str]:
        pass

    def can_handle_post_instruction(self) -> bool:
        return False

    def post_instruction(self, response: str) -> str:
        pass

    def can_handle_pre_command(self) -> bool:
        return False

    def pre_command(
            self, command_name: str, arguments: Dict[str, Any]
    ) -> Tuple[str, Dict[str, Any]]:
        pass

    def can_handle_post_command(self) -> bool:
        return False

    def post_command(self, command_name: str, response: str) -> str:
        pass

    def can_handle_chat_completion(
            self, messages: Dict[Any, Any], model: str, temperature: float, max_tokens: int
    ) -> bool:
        return False

    def handle_chat_completion(
            self, messages: List[Message], model: str, temperature: float, max_tokens: int
    ) -> str:
        pass
