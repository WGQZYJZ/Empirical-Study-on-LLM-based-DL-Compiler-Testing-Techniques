
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v0 = self.attn(x1).transpose(-2, -1) # [B, 64, 3]
        scale = math.sqrt(v0.size(-1)) # 1.7079458 
        v1 = v0 / scale # [B, 64, 3]
        v2 = v1 + 1 # [B, 64, 3]
        return v2


# Initializing the model