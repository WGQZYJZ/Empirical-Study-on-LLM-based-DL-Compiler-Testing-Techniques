
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = torch.nn.functional.conv3d(x1, self.linear.weight, bias=self.linear.bias, stride=(1, 1, 1))
        v2 = torch.nn.functional.conv3d(x2, self.linear.weight, bias=self.linear.bias, stride=(1, 1, 1))
        return torch.cat((v1, v2), dim=-1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 3, 4, 5)
x2 = torch.randn(2, 2, 3, 4, 5)
