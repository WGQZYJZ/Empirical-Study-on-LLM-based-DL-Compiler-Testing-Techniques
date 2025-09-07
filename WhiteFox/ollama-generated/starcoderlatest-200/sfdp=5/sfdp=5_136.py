
class Model(torch.nn.Module):
    def __init__(self, k, v):
        super().__init__()
        self.k = k # Key dimension
        self.v = v # Value dimension
 
    def forward(self, q, x1):
        d_q  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key
        d_k = torch.softmax(d_q, dim=-1) * (attn_mask + attn_mask.transpose(-2,-1)).log() # Apply softmax to the dot product scaled by the attention mask and log it
        a = torch.matmul(a, d_k)  # Compute the dot product of the dropout output and the value
        return output

# Initializing the model
m = Model(8, 32)

# Inputs to the model
q = torch.randn(1, k, 64, 64)
x1 = torch.randn(1, v, 64, 64)
