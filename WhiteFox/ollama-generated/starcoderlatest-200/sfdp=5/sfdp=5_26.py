
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(128, 32)
 
    def forward(self, x1, x2):
        qk = self.attn(x1, x2)[0]
        return qk


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(128, 128, 3, 64)
x2 = torch.randn(256, 128, 3, 64)
