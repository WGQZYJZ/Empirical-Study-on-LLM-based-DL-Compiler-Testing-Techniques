
class Model(torch.nn.Module):
    def __init__(self, args):
        super().__init__()
        self.conv = torch.nn.Conv2d(args.hidden_size, 8, 1, stride=1, padding=0)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = x2 * v5
        return v6

# Initializing the model
m = Model(args)


