qk = query * key.T # Compute the dot product of the query and key tensors by transposing the key tensor
attn_weight  = torch.softmax(qk / math.sqrt(key.size(-1)), dim=-1)  # Apply softmax to the scaled dot-product, where the scaling factor is the square root of the number of columns in the key tensor (-1)
output  = attn_weight @ value.T  # Compute a weighted sum of the value tensors by taking the dot product of the attention weights with the transposed version of the value tensor, which reshapes them to match the dimensions of the query and value tensors.
