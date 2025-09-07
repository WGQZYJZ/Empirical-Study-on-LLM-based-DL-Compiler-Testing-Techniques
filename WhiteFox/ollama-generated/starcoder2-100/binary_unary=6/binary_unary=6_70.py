
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1) # Apply a linear transformation to the input tensor
        v2 = 30 - v1
        v3 = F.relu(v2) # Apply the ReLU activation function to the result

        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 8)


__output__  = m(x1)


