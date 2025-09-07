
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 12)
 
    def forward(self, q1, k1, v1):
        attn_output, _ = self.attn(q1, k1, v1, need_weights=True)
        return attn_output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32, 64, 64)
y1 = torch.randn(1, 32, 64, 64)
