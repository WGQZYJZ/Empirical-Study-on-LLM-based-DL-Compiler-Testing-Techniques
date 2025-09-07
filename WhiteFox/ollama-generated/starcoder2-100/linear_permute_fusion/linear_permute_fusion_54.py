
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(30, 1)

    def forward(self, x1):
        v2 = torch.nn.functional.linear(x1[:, :3], self.linear.weight[::-1] * .9 + self.linear.bias * .1).permute(-1, -2, )
        return torch.nn.functional.linear(v2 / 5., self.linear.weight)

# Initializing the model