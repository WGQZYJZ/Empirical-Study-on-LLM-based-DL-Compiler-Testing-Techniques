
class Model(torch.nn.Module):
    def __init__(self, dim=16):
        super().__init__()
        self.linear = torch.nn.Linear(dim, 4)
 
    def forward(self, x1, other):
        v1 = self.linear(x1) + other  # Apply a linear transformation to the input tensor
        return v1


# Initializing the model
m = Model()

