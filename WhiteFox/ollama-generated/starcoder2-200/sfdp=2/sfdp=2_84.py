qk  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(torch.tensor([key_hidden]))  # Compute the dot product between query and key
softmax_qk = qk.softmax(dim=-1)  # Apply softmax to the dot product of query and key
output = torch.matmul(value, softmax_qk) * value  # Compute the dot product of the value and the softmax output, then multiply that output by itself.
