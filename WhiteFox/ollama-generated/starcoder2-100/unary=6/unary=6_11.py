class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # Initializing the model
        t1 = self.conv(x1)
        v2 = torch.clamp_min(t1 + 3, 0)
        v3 = torch.clamp_max(v2, 6)
        v4 = t1 * v3
        return v4
