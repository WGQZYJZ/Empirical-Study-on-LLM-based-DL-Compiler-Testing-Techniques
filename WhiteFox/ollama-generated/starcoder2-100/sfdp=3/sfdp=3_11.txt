
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(512, 8)
 
    def forward(self, x1):
        v1, v2 = self.attn(x1, None, scale_factor=0.67344930305856326)
        return v2


# Initializing the model