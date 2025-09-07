
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        return v1.permute(0, 2, 1)


# Initializing the model
m = Model()
x1 = torch.randn(1, 2, 3, 4)  # In case of PyTorch version lower than v1.8, you should manually convert x1 from numpy to tensor with permute method.
