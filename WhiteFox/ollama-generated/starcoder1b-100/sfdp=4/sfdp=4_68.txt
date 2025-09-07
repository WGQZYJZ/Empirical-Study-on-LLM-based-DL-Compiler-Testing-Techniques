
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(x1.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = torch.matmul(attn_weight, x2) # Compute the dot product of the attention weights and the value
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
