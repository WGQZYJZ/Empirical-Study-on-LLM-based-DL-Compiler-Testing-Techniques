
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk * scale_factor # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 32, 512, 8) # (batch_size, num_heads, head_dim, seq_length)
key = torch.randn(1, 32, 512, 8) # (batch_size, num_heads, head_dim, seq_length)
value = torch.randn(1, 32, 512, 8) # (batch_size, num_heads, head_dim, seq_length)
