
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(2, 3, 1)

    def forward(self, x1):
        bn = torch.nn.functional.batch_norm(x1, self.conv.weight, self.conv.bias, self.conv.groups, True, True)
        return bn

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2, requires_grad=True)
