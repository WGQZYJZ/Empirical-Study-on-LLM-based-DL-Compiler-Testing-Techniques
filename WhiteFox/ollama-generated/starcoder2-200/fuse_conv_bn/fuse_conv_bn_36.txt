
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.conv3d(x1, self.linear.weight)
        return v

