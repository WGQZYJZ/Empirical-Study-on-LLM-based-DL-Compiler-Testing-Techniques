
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.relu(x1) # Apply the unary operation to each point of the input tensor
        return v


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(32, ...)


