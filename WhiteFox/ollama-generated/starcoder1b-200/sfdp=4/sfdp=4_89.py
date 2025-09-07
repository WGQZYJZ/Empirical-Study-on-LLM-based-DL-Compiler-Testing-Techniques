
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, attn_mask):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = (attn_mask * v2) * (attn_mask * v5)  # (v1, v1) @ [0.5] * [0.5] = [0.25] * [0.75], which is (x1, x1) + [0.5].
        return v6


# Initializing the model
m = Model()


