
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 32)
 
    def forward(self, q, k, v, s):
        qk = torch.matmul(q, k.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk.div(s) # Scale the dot product by a scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = self.attention(q, k, v, dropout_qk)[0] # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
q  = torch.randn(1, 32, 64, 64)
k  = torch.randn(1, 32, 64, 64)
v  = torch.randn(1, 32, 64, 64)
s  = torch.randint(0, 8, (1,)).item() # Scale factor
