
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(768, 128)
 
    def forward(self, x1):
        qk = x1 @ x1.transpose(-2, -1) / math.sqrt(x1.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        v = self.qkv(attn_weight)
        output = (attn_weight * v).sum((2, 3)) # Compute the dot product of the attention weights and the value
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(512, 768)
