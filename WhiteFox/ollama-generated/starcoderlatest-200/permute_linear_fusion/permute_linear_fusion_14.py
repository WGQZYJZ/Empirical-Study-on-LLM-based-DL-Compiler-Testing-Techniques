
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        t2 = torch.cat((v1, v1), dim=2)
        t2 = t2.transpose(0, 1)
        v3 = torch.nn.functional.linear(t2, self.linear.weight, self.linear.bias)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
