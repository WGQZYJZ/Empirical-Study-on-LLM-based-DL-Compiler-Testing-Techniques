
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(1, 32)
 
    def forward(self, qk):
        v6, _ = self.attention(qk[0], qk[1], qk[2])
        return v6

# Initializing the model
m = Model()

# Inputs to the model
qk1 = (torch.randn(32, 3, 512), torch.randn(32, 32, 512))
qk2 = (torch.randn(32, 3, 512), torch.randn(32, 32, 512))
qk3 = (torch.randn(32, 3, 512), torch.randn(32, 32, 512))
