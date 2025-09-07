
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 16)
 
    def forward(self, x1, x2):
        y1, _ = self.attn(x1, x2, x2)
        return y1


# Inputs to the model
x1 = torch.randn(1, 3, 500, 500)
x2 = torch.randn(8, 3, 64, 64)
