
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, attention_mask):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        attn_weight = torch.softmax(qk, dim=-1) * (value / math.sqrt(query.size(-1)))
        return attn_weight @ output

 # Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
attention_mask = torch.zeros((1, 3, 64, 64), dtype=torch.bool)
