
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(8, 4, bias=False)
 
    def forward(self, q1, k1, v1, attn_mask1):
        b, t, c, h = q1.size()
        w = self.attn(q1).view(b, t, -1).permute(0, 2, 1)
        s = torch.matmul(w, k1) / math.sqrt(v1.size(-1)) # Compute the dot product of q and k, and scale it
        attn_weight = F.softmax(s, dim=-1)  # Apply softmax to the result
        output = torch.matmul(attn_weight, v1)  # Compute the dot product of the attention weights and the value
        return output, attn_weight
 

# Initializing the model
m = Model()

 # Inputs to the model
q1 = torch.randn(32, 4, 64, 64)
k1 = torch.randn(32, 4, 32, 32)
v1 = torch.randn(32, 4, 32, 32)
attn_mask1 = (torch.randn(1) < 0.8).expand(-1, -1, -1, -1).to(dtype=torch.bool)
__output__, __attn_weight__ = m(q1, k1, v1, attn_mask1)

 