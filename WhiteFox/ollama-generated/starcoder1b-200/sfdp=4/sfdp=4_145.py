
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        qk = self.conv(x1) / math.sqrt(x1.size(-1))  # Compute the dot product of the query and key, and scale it
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        value = self.conv(x1) * attn_weight # Compute the dot product of the attention weights and the value
        return value


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
