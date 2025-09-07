
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = Attention(8, 3)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(float(math.pow(len(x1), 0.5) * len(x2)))
        output = self.attn(qk, x1, x2)
        return output

# Initializing the model
m = Model()

# Inputs to the model
query_tensor = torch.randn(1, 3, 64, 64)  # Query input (for this layer)
key_tensor = torch.randn(2, 8, 64, 64)   # Key input (for this layer)
value_tensor = torch.randn(2, 8, 64, 64)   # Value input (for this layer)
