
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, attn_mask):
        v1 = torch.matmul(attn_mask, x2) / math.sqrt(attn_mask.size(-1)) + x1
        return v1


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
attn_mask = torch.randn(1, 64, 64, 64)
