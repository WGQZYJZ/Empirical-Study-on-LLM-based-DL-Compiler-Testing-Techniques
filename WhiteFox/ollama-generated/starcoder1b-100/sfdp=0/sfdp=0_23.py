for i in range(N):
    alpha[i] = exp(-(query - key) * inv_scale)  # Compute softmax for each input instance
out = torch.matmul(x1, alpha)                   # Take dot product of each input instance and its attention weights (softmax of the scaled dot product between the query and key tensors)
attention_weights = out / exp(scaled_dot_product - log_sum_exp(out))  # Compute attention weights for each input instance using softmax function
output = torch.matmul(attention_weights, value)       # Take weighted sum of values
