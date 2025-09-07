
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(1, 8)
 
    def forward(self, x1, x2):
        qk, _ = self.attn(x1, x2, x2)
        return qk


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 16, 32, 64)
x2 = torch.randn(8,  16, 64, 64)
