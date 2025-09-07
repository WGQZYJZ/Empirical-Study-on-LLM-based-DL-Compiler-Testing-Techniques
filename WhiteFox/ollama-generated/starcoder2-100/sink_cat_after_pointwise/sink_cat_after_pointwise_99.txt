
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.relu(x1) # Apply a pointwise unary operation to the input tensor
        v2 = torch.cat([v1], dim=0).view(-1, 256, 4, 4) 
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.rand(10, 3, 8) # Input with the shape of [10 x 3 x 8] 
