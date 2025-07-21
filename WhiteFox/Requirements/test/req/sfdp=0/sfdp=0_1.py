# Calculate the scaled dot-product attention
# Compute the attention scores by multiplying query with the transposed key
attention_scores = torch.matmul(query, key.transpose(-2, -1))

# Scale the attention scores
scaled_attention_scores = attention_scores.div(inv_scale)

# Apply the softmax function to obtain attention weights
attention_weights = scaled_attention_scores.softmax(dim=-1)

# Multiply the attention weights by the value tensor
attention_output = attention_weights.matmul(value)
