
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(32*1508, 64)

    def forward(self, x1):
        v1 = self.lin(x1) # Applying a linear transformation to the input tensor.
        v2 = nn.ReLU()(v1) # Applying the ReLU activation function to the output of the linear transformation.
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3*1508)
__output__  = m(x1)

