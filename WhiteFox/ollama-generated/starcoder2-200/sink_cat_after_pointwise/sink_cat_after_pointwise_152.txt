

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.relu(x1)  # Apply ReLU to the input tensor
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(100, 256*784/256) + 1
