
class Model(torch.nn.Module):
    def __init__(self, d_in=32, d_out=16):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, d_in // 2, 1)
        self.fc    = torch.nn.Linear(d_in // 4, d_out)
 
    def forward(self, x1, x2):
        x  = self.conv(x1)
        v = torch.cat([x, x], dim=-1)
        v = self.fc(v)
        return v


# Initializing the model
m = Model()


