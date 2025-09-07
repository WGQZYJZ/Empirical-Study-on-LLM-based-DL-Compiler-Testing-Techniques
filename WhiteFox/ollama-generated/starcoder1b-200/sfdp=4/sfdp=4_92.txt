
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        qk = torch.einsum("ni,ni->ni", x1, v2) / torch.sqrt(v2.size(-1))
        attn_weight = torch.softmax(qk, dim=-1)
        return attn_weight @ value


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
