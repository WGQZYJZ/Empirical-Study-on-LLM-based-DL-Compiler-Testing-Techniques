
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 8) # Input query
        self.key = torch.nn.Linear(3, 8) # Key tensor
        self.value = torch.nn.Linear(3, 8) # Value tensor
 
    def forward(self, x1):
        v = (x1 * (2.0 / torch.norm(x1)**2)).view(-1, 3, 4, 64).transpose(2, 3).contiguous()
        qk = self.query(v) @ self.key.transpose(-2, -1) / math.sqrt(self.query.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        return attn_weight @ self.value # Compute the dot product of the attention weights and the value
 

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
