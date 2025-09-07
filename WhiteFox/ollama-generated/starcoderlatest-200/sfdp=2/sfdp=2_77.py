v2  = linear(k) # Compute a matrix multiplication between a tensor with shape (batch_size, hidden_dim) and another tensor with shape (hidden_dim, batch_size), the result has the shape of (hidden_dim, batch_size)
output  = torch.matmul(q, v2) # Matrix multiplication between q and the output of the linear transformation k
qk  = torch.matmul(query, key) # Compute the dot product of the query and the key
scaled_qk  = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
output  = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value
