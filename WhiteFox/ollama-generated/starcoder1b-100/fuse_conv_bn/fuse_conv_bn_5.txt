
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        output = self.linear(x1).transpose(0, 1)
        return output


# Inputs to the model
x1 = torch.randn(1, 2, 2)
