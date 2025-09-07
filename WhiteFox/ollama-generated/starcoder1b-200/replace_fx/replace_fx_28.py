
class Model(torch.nn.Module):
    def __init__(self, replace=True):
        super().__init__()
        if replace:
            self.linear  = torch.nn.Linear(2, 2)
        else:
            self.linear  = lambda x1: x1

    def forward(self, x1):
        return self.linear(x1)


# Inputs to the model
input_tensor = torch.randn(1, 2, 3, 4)
