
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.Linear()(x1)  # Linear transformation to an input tensor
        v2 = v1 - other

        return v2

# Initializing the model
m = Model()


# Inputs to the model
other = torch.randn(30, 30)
x1 = torch.randn(40, 56)
