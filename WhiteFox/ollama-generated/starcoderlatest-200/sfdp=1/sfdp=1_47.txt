
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 16)
 
    def forward(self, x1, x2):
        qk = self.attention(x1, x2)
        output = self.attention(qk[0], qk[1])
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(16, 8, 32, 32)
x2 = torch.randn(16, 8, 16, 16)
