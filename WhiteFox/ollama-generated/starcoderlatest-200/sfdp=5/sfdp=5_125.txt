
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(10, 8)
 
    def forward(self, x1, x2):
        qk = (x1 @ x2.transpose(-2, -1)) / math.sqrt(x1.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = (attn_weight * x2).sum(dim=1) # Sum all entries in dimension 1
        return output

# Inputs to the model
x1 = torch.randn(16, 10, 100) 
x2 = torch.randn(16, 8, 100)
