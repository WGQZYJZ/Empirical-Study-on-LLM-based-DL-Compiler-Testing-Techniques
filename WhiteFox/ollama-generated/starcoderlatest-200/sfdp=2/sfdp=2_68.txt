
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, x1, x2, x3):
        qk, v, _  = self.attn(x1, x2, x3)
        output = torch.matmul(qk, v)
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(16, 3, 64, 64) # The query tensor
x2 = torch.randn(16, 8, 64, 64) # The key tensor
x3 = torch.randn(16, 8, 64, 64) # The value tensor
