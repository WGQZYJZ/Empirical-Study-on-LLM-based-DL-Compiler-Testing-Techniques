scaled_dot_qk  = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
scaled_dot_qk = scaled_dot_qk / math.sqrt(float(n_head))
output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
