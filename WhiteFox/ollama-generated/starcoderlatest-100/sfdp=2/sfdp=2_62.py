
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 16)
 
    def forward(self, x1, x2):
        _, attn_output = self.attention(x1, x2, x2)
        return attn_output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 8, 64, 64)
x2 = torch.randn(32, 8, 64, 64)
