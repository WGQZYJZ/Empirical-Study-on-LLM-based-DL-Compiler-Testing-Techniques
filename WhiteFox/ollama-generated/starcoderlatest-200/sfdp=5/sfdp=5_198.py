
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multihead_attention = torch.nn.MultiheadAttention(512, 8)

    def forward(self, x1, x2):
        y1, _  = self.multihead_attention(x1, x2)
        return y1

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(256, 512, 64, 64)
x2 = torch.randn(256, 512, 64, 64)
