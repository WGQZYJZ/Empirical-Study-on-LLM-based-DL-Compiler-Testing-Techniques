
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(64 * 64, 8)
        self.relu  = torch.nn.ReLU()

    def forward(self, x1):
        v1  = self.linear(x1) # Apply a linear transformation to the input tensor
        v2  = self.relu(v1) # Apply the ReLU activation function to the output of the linear transformation
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 64 * 64)
__output__   = m(x1)


