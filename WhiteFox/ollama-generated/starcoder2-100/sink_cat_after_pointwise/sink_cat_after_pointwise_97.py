
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):
        v1 = torch.cat([x1, y2], dim=0) # Concatenate tensors along a dimension
        v2 = torch.relu(v1)              # Apply pointwise ReLU operation to the reshaped tensor
        return v2

# Initializing the model
m  = Model()

# Inputs for the model
x1 = torch.rand([50, 64])
y2 = torch.rand([3, 64])

 # Initialize and run the model with inputs x1 and y2
__output__  = m(x1, y2)

