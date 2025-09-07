
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query_tensor, key_tensor):
        qk = torch.matmul(query_tensor, key_tensor) # Compute the dot product of the query and the key
        scaled_qk = qk / math.sqrt(key_tensor.size(-1)) # Scale the dot product by sqrt(value dimensions)
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value_tensor) # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
query_tensor = torch.randn(batch_size, num_heads, seq_length, embedding_dim)
key_tensor = torch.randn(batch_size, num_heads, key_seq_length, embedding_dim)
