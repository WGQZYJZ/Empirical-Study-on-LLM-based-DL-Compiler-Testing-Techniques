
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 3)

    def forward(self, x):
        v0  = self.linear(x) # Apply linear transformation to input tensor

        return v0


# Initializing the model
m = Model()


# Inputs to the model
x = torch.rand(1,256)

__output__= m(x)


