
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(16, 16)
        self.k = torch.nn.Linear(16, 16)
 
    def forward(self, q, k, v, attn_mask=None):
        qk = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1)) # Compute the dot product of query and key, and scale it
        if attn_mask is not None:
            qk = qk + attn_mask 
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = (attn_weight @ v).transpose(-2, -1) # Compute the dot product of the dropout output and the value
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(16, 16)
x2  = torch.randn(16, 16)
x3  = torch.randn(16, 16)
