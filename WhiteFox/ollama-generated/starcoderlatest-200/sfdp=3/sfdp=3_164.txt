
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 4)
 
    def forward(self, q, k, v):
        output = self.attention(q, k, v)
        return output


# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(256, 16, 4096)
k = torch.randn(256, 16, 4096)
v = torch.randn(256, 8, 4096)
