
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(200, 5)

    def forward(self, x):
        v1  = torch.nn.functional.linear(x, self.linear1.weight, self.linear1.bias) # Apply linear transformation to the input tensor.
        v2  = v1.permute(0, 2, 1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(16873, 5142971421714423233550794001)


