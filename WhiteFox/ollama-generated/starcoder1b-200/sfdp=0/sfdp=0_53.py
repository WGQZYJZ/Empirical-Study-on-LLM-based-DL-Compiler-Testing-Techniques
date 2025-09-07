
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.linear = torch.nn.Linear(3 * 64 * 64, 3)
 
    def forward(self, x):
        q1 = x[:, :, None, None]  # [B, L, 1, 1]
        k2 = self.conv(q1).contiguous()  # [B, L, Cin, Ci]
        v = torch.tensordot(k2, x, dims=[-1, -2])  # [B, Cout, L]
        o = self.linear(torch.cat([v, x], dim=-1))  # [B, Cout * L]
        return o


# Initializing the model
m = Model()

