
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, attn_mask):
        vq = (x1 @ x2.transpose(-2, -1) / math.sqrt(x1.size(-1))) + attn_mask
        return torch.softmax(vq, dim=-1) @ x2

# Inputs to the model
x1 = torch.randn(16, 50)
x2 = torch.randn(16, 48)
attn_mask = torch.randint(low=0, high=16, size=(16, 1), dtype=torch.bool)
