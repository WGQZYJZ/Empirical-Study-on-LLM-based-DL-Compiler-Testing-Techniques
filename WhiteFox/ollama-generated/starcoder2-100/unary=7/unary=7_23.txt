
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 32)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * F.clamp(min=0, max=6, input=v1 + 3).div(6) # Clamp the output of the linear transformation added with 3 and divide it by 6
        return v2
