
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)  # Concatenate the two tensors along dimension 0
        v2 = v1.view(-1, 4)          # Reshape tensor 'v1' into a single-dimension array
        return self.relu(v2)        # Apply unary operation on the reshaped array


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 3)
x2 = torch.randn(3, 2)
