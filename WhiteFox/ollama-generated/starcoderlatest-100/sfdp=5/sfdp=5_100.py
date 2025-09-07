
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_qkv = torch.nn.Linear(256, 2 * 3 * 32, bias=False)
        self.attn_out = torch.nn.Conv2d(8, 32, 1, stride=1, padding=0)
 
    def forward(self, x1, x2):
        v1 = self.attn_qkv(x1).reshape(256, -1, 32, 3, 3).permute(0, 1, 4, 2, 3, 5)
        v2 = self.attn_out(v1)
        return torch.matmul(v2, x2.permute(0, 1, 3, 4, 2))

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 256, 8, 32, 32) # 4*4
x2 = torch.randn(1, 16, 8, 32, 32) # 4*4
