const prompts = [
  "Ask Copilot to scaffold unit tests that describe the behavior you expect before refactoring.",
  "Use inline chat: 'Document this function with a docstring that highlights business rules.'",
  "Prompt Copilot to suggest accessibility improvements for the current page's HTML.",
  "Request a refactor: 'Simplify this endpoint and highlight risky changes in comments.'",
  "Experiment with pair-debugging: 'Why might this fetch handler fail on slow networks?'"
];

const button = document.getElementById("prompt-idea");
const ideaBox = document.getElementById("idea");

const getRandomPrompt = () => prompts[Math.floor(Math.random() * prompts.length)];

button?.addEventListener("click", () => {
  ideaBox.textContent = getRandomPrompt();
});
