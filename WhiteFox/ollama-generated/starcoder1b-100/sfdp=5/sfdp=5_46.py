context_vector  = softmax(W1(X) @ W2(X))  # Compute context vector using self-attention weights
output  = X + V * attention.tanh(context_vector)
output  = softmax(W1(X) @ W2(X))  # Compute output matrix W(X), apply tanh to the result, and then multiply it with V * attention.tanh(context_vector)
