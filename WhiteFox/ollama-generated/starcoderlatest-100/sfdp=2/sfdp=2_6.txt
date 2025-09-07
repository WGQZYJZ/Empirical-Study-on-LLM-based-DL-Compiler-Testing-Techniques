
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 32)

    def forward(self, query, key, value):
        qk = self.attention(query, key, value) # Compute the attention using MultiheadAttention
        return qk

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 8, 64, 64)
x2 = torch.randn(2, 32, 64, 64)
x3 = torch.randn(2, 8, 64, 64)
