
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(20, 5)
        self.key   = torch.nn.Linear(14, 8)
        self.value = torch.nn.Linear(14, 9)
 
    def forward(self, x1, x2):
        qk   = self.query(x1) @ self.key(x2).transpose(-2, -1) / math.sqrt(x1.size(-1)) # Compute the dot product of the query and key tensors, and scale them
        attn_weight  = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ self.value(x2) # Compute the dot product of the attention weights and the value tensor
        return output

# Initializing the model
m = Model()

# Inputs to the model
q  = torch.randn(1, 20) # Query tensor
k  = torch.randn(3, 14) # Key tensor
v  = torch.randn(1, 9)   # Value tensor
x1 = torch.randn(1, 64, 64) # Input tensor
x2 = torch.randn(1, 16, 16) # Query tensor
