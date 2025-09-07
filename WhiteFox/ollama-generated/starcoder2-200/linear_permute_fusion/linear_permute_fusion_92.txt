
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)

    def forward(self, x2):
        v2  = torch.nn.functional.linear(x2) # Apply linear transformation to the input tensor.
        return v2.permute(0, 2, 1)


# Initializing the model
m  = Model()


# Inputs to the model
x2  = torch.randn(3)


__output__  = m(x2)
