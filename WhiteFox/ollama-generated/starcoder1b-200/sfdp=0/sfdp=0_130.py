scaled_dot_product = torch.matmul(query, key) / math.sqrt(key.size(-1))
attention_weights = torch.softmax(scaled_dot_product, dim=-1)
output = torch.matmul(value, attention_weights).squeeze(-2)  # Reshape the output to match the shape of the input to prevent gradient vanishing
