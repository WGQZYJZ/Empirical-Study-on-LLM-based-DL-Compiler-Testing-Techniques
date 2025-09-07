
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(256, 10)

    def forward(self, x1):
        v1  = self.linear(x1) # Apply a linear transformation to the input tensor
        v2  = v1 + other_tensor
        v3  = torch.relu(v2) # Apply ReLU activation function to the output of the linear transformation plus another tensor
        return v3


# Initializing the model
m = Model()
other_tensor  = torch.randn(256, 10) # Any valid 4D PyTorch tensor


# Inputs to the model:
x1  = torch.randn(1, 256)
__output__  = m(x1)


