
class Model(torch.nn.Module):
    def __init__(self, k=32):
        super().__init__()

    def forward(self, x1):
        v1  = torch.cat([x1, self.__input__], dim=-1) # Concatenate the input tensor with an additional channel dimension
        v2  = v1.view(-1, int(__input__.size(-1))) # Reshape along a single dimension by inserting a size of -1.
        v3  = torch.relu(v2)                          # Apply ReLU unary operator to the reshaped tensor.
        return v3

# Initializing the model
m = Model()

# Input to the model
x1  = torch.randn(5, 4)

__output__  = m(x1)

