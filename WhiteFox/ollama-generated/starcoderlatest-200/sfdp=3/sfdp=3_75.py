
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(1, 8)) # key dim : (seq_len, batch_size, heads, head_dim) 
        self.key   = torch.nn.Parameter(torch.randn(1, 32, 64, 64))
        self.value = torch.nn.Parameter(torch.randn(1, 32, 64, 64))
 
    def forward(self):
        qk = torch.matmul(query, key) # Compute the dot product of the query and key tensors
        scaled_qk = qk * scale_factor # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk * value # Compute the dot product of the dropout output and the value tensor
        return output
 

# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(1, 8) # (seq_len, batch_size, heads, head_dim)
key    = torch.randn(1, 32, 64, 64)
value  = torch.randn(1, 32, 64, 64)
