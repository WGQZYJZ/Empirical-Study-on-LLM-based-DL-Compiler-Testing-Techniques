
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.value_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.key_conv(x1)
        qk = torch.einsum('bnchw,bnchw->bcnhw', (x1, v1)) / math.sqrt(v1.size(-1))
        attn_mask  = torch.ones_like(qk).float()
        output = torch.einsum('bcnhw,bcnhw->bnchw', (attn_weight * value, v6))
 
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
