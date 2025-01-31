from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_ollama import ChatOllama



# Create a ChatOllama model
model = ChatOllama(model="deepseek-r1")

# SystemMessage:
#   Message for priming AI behavior, usually passed in as the first of a sequenc of input messages.
# HumanMessagse:
#   Message from a human to the AI model.
messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
]

# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")


# AIMessage:
#   Message from an AI.
messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
    AIMessage(content="81 divided by 9 is 9."),
    HumanMessage(content="What is 10 times 5?"),
]

# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")


# output
#Answer from AI: <think>
# I need to divide 81 by 9.
#
# First, I recognize that division involves finding how many times one number can be subtracted from another until it reaches zero.
#
# In this case, I'll start with 81 and repeatedly subtract 9 until the result is zero. Each subtraction represents a single unit of the divisor.
#
# After performing the subtraction nine times, I reach zero.
#
# Therefore, the division of 81 by 9 results in 9.
# </think>
#
# To solve \( \frac{81}{9} \), follow these steps:
#
# 1. **Understand Division:**
#    Division is about finding how many times one number (divisor) can be subtracted from another (dividend) until the remainder is zero.
#
# 2. **Set Up the Problem:**
#    \[
#    \frac{81}{9}
#    \]
#
# 3. **Divide 81 by 9:**
#    Determine how many times 9 fits into 81.
#
#    - \(9 \times 1 = 9\)
#    - \(9 \times 2 = 18\)
#    - \(9 \times 3 = 27\)
#    - \(9 \times 4 = 36\)
#    - \(9 \times 5 = 45\)
#    - \(9 \times 6 = 54\)
#    - \(9 \times 7 = 63\)
#    - \(9 \times 8 = 72\)
#    - \(9 \times 9 = 81\)
#
# 4. **Find the Quotient:**
#    From the multiplication table, we see that \(9 \times 9 = 81\).
#
# 5. **Conclusion:**
#    Therefore,
#    \[
#    \frac{81}{9} = 9
#    \]
#
# **Final Answer:**
# \[
# \boxed{9}
# \]
# Answer from AI: <think>
# Alright, so I'm trying to figure out what 10 times 5 is. Okay, let's break this down step by step. First off, multiplication is basically repeated addition, right? So when you multiply two numbers, you're adding one of them a certain number of times.
#
# In this case, it's 10 multiplied by 5. So that means I need to add the number 10 five times. Let me write that out: 10 + 10 + 10 + 10 + 10. Hmm, adding all those together should give me the answer.
#
# Let me do the addition step by step to make sure I'm not making a mistake:
# - First addition: 10 + 10 = 20
# - Second addition: 20 + 10 = 30
# - Third addition: 30 + 10 = 40
# - Fourth addition: 40 + 10 = 50
#
# So, after adding 10 four more times to the initial 10, I end up with 50. Wait a minute, that's five tens, right? So 10 times 5 should indeed be 50.
#
# Just to double-check, maybe there's another way to look at it. I know that multiplication can also be thought of as scaling or grouping objects. If I have 10 groups and each group has 5 items, the total number of items would be 10 times 5. So if each group is 5, then:
# - Group 1: 5
# - Group 2: 10 (5+5)
# - Group 3: 15 (10+5)
# - Group 4: 20 (15+5)
# - Group 5: 25
#
# Wait, that's only five groups and I'm getting to 25. That doesn't match my previous result of 50. Did I make a mistake somewhere?
#
# Let me try another approach using the standard multiplication algorithm. Multiplying 10 by 5:
# ```
#    10
# x  5
# -----
#    50
# ```
# So that gives me 50 again. Hmm, now I'm confused because earlier when I thought of 10 groups of 5, it added up to 25 instead of 50.
#
# Oh wait, maybe I miscounted the groups before. Let's try that again with clearer steps:
# - Group 1: 5
# - Group 2: 10 (5+5)
# - Group 3: 15 (10+5)
# - Group 4: 20 (15+5)
# - Group 5: 25 (20+5)
#
# Wait, that's still only 25. That can't be right because I know 10 times 5 is 50 from previous knowledge. Where did I go wrong?
#
# Maybe the issue is how I'm conceptualizing the groups. If each group has 5 items and there are 10 groups, then it should be:
# - Group 1: 5
# - Group 2: 10 (5+5)
# - Group 3: 15 (10+5)
# - Group 4: 20 (15+5)
# - Group 5: 25 (20+5)
# - Group 6: 30 (25+5)
# - Group 7: 35 (30+5)
# - Group 8: 40 (35+5)
# - Group 9: 45 (40+5)
# - Group 10: 50 (45+5)
#
# Ah, there we go! I see where I messed up earlier. I only counted five groups instead of ten. So when you have 10 groups of 5, adding them all together gives you 50.
#
# Another way to confirm this is by using the distributive property:
# - 10 times 5 can be thought of as (9 + 1) times 5.
# - Which is 9 times 5 plus 1 times 5.
# - So that's 45 plus 5, which equals 50.
#
# This makes sense because if you know that 9 times 5 is 45, adding another 5 gives you the total of 50. That checks out with my earlier calculation using multiplication.
#
# I think I was just initially miscounting when trying to visualize the groups in my head. But by carefully going through each step and double-checking with different methods like addition and distribution, I've arrived at the correct answer consistently: 50.
# </think>
#
# 10 multiplied by 5 equals **50**.
#
# **Step-by-Step Explanation:**
#
# 1. **Understanding Multiplication:** Multiplying two numbers involves adding one of the numbers a certain number of times (as specified by the other number). In this case, multiplying 10 by 5 means adding 10 five times.
#
# 2. **Repetitive Addition Approach:**
#    - 10 + 10 = 20
#    - 20 + 10 = 30
#    - 30 + 10 = 40
#    - 40 + 10 = 50
#
# 3. **Grouping Method:** Consider having 10 groups, each containing 5 items:
#    - Group 1: 5
#    - Group 2: 10 (5+5)
#    - Group 3: 15 (10+5)
#    - Group 4: 20 (15+5)
#    - Group 5: 25 (20+5)
#    - Group 6: 30 (25+5)
#    - Group 7: 35 (30+5)
#    - Group 8: 40 (35+5)
#    - Group 9: 45 (40+5)
#    - Group 10: 50 (45+5)
#
# 4. **Distributive Property:** Break down the multiplication:
#    - 10 × 5 = (9 + 1) × 5
#    - = (9 × 5) + (1 × 5)
#    - = 45 + 5
#    - = 50
#
# By using these methods, we consistently arrive at the result of **50**.
#
# Process finished with exit code 0