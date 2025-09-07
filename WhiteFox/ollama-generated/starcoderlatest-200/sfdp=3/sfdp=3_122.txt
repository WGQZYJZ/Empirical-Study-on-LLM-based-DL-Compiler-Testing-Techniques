
class Transformer(torch.nn.Module):
    def __init__(self, num_heads, hidden_size):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=16, num_heads=8)
 
    def forward(self, x1, x2):
        qk  = torch.matmul(x1, x2.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk  = qk.mul(0.5) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.4) # Apply dropout to the softmax output
        output  = dropout_qk.matmul(x2) # Compute the dot product of the dropout output and the value tensor
        return output

# Initializing the model
t = Transformer(8, 16)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
