
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 2, dropout=0)
 
    def forward(self, x1, x2):
        y1, attn_weights = self.attn(x1, x2, x2, need_weights=True)
        return y1

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
