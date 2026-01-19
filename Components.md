# LangChain Components
**LangChain** is an open source framework with a pre-built agent architecture and integrations for any model or tool, so you can build agents that adapt as fast as the ecosystem evolves.
**LangChain** is the easiest way to start building agents and applications powered by LLMs. With under 10 lines of code, you can connect to OpenAI, Anthropic, Google and more. **LangChain** provides a pre-built agent architecture and model integrations to help you get started quickly and seamlessly incorporate LLMs into your agents and applications.

## **1. Models**
Models are the core interfaces through which you interact with AI models. Two types:
1. Language Models (text -> text), chatbot
2. Embedding Models (text -> vector), semantic search

## **2. Prompts**
LLMs -> inputs -> prompts
1. Dynamic and Reusable Prompts
2. Role-based Prompts
3. Few shot Prompting

## **3. Chains**
Chains act as step-by-step workflows that complete tasks in sequence.
1. Sequential
2. Parallel
3. Conditional etc.

## **4. Indexes**
1. Doc loader
2. Text split
3. Vector store
4. Retriever

## **5. Memory**
Memory is a system that remembers information about previous interactions. For AI agents, memory is crucial because it lets them remember previous interactions, learn from feedback and adapt to user preferences.
LLM API calls are stateless, it doesn't store any previous interactions. So langchain memory solve this problem.
1. Conversation Buffer Memory
2. Conversation Buffer Window Memory
3. Summarizer-based Memory
4. Custom Memory

## **6. Agents**
Agents combine language models with tools to create systems that can reason about tasks, decide which tools to use and iteratively work towards solutions.

