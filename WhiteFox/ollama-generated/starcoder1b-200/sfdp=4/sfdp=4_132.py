
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = self.conv(x1) * 0.7071067811865476
        v3 = torch.erf(v2)
        v4 = v3 + 1
        qk  = v2 @ x1  # Compute the dot product of the query and key, and scale it
        attn_weight  = torch.softmax(qk / math.sqrt(x1.size(-1)), dim=-1)  # Apply softmax to the result
        value = attn_weight @ v1  # Compute the dot product of the attention weights and the value
        return value

# Initializing the model
m = Model()


