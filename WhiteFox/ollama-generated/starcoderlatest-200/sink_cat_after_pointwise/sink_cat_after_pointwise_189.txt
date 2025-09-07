
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=0) # Sink a cat operation to the input tensor
        v2 = v1.view(-1)               # Reshape after sinking
        v3 = torch.relu(v2)           # Apply relu function
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 4)
