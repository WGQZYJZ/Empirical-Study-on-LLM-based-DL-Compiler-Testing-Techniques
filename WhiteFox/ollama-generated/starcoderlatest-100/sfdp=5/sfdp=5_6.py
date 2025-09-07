
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, qk1, v1):
        attn_output, _ = self.attn(qk1, v1, v1)
        return attn_output


# Initializing the model
m = Model()
# Inputs to the model
qk1 = torch.randn(2, 3, 64, 64)
v1 = torch.randn(2, 8, 64, 64)
