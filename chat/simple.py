
from langchain_ollama import ChatOllama


# Create a ChatOpenAI model
model = ChatOllama(model="deepseek-r1")

# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)

# output:
# Full result:
# content="<think>\nFirst, I need to determine how many times 9 can fit into 81.\n\nI know that multiplying 9 by 9 gives me exactly 81.\n\nTherefore, the result of dividing 81 by 9 is 9.\n</think>\n\nTo divide **81** by **9**, follow these steps:\n\n1. **Understand Division**: Division tells you how many times one number can be divided into another. In this case, we're finding out how many groups of 9 are in 81.\n\n2. **Multiply to Check**:\n   - Think about what number multiplied by 9 gives 81.\n   - \\( 9 \\times 9 = 81 \\)\n\n3. **Conclusion**: Since multiplying 9 by 9 equals 81, there are **9 groups of 9** in 81.\n\n\\[\n\\boxed{9}\n\\]" additional_kwargs={} response_metadata={'model': 'deepseek-r1', 'created_at': '2025-01-31T13:14:25.883068137Z', 'done': True, 'done_reason': 'stop', 'total_duration': 7627837648, 'load_duration': 3419938796, 'prompt_eval_count': 13, 'prompt_eval_duration': 155000000, 'eval_count': 188, 'eval_duration': 4049000000, 'message': Message(role='assistant', content='', images=None, tool_calls=None)} id='run-556e733f-c0b3-4cfa-b4be-66b004a39ccd-0' usage_metadata={'input_tokens': 13, 'output_tokens': 188, 'total_tokens': 201}
# Content only:
# <think>
# First, I need to determine how many times 9 can fit into 81.
#
# I know that multiplying 9 by 9 gives me exactly 81.
#
# Therefore, the result of dividing 81 by 9 is 9.
# </think>
#
# To divide **81** by **9**, follow these steps:
#
# 1. **Understand Division**: Division tells you how many times one number can be divided into another. In this case, we're finding out how many groups of 9 are in 81.
#
# 2. **Multiply to Check**:
#    - Think about what number multiplied by 9 gives 81.
#    - \( 9 \times 9 = 81 \)
#
# 3. **Conclusion**: Since multiplying 9 by 9 equals 81, there are **9 groups of 9** in 81.
#
# \[
# \boxed{9}
# \]
#
# Process finished with exit code 0