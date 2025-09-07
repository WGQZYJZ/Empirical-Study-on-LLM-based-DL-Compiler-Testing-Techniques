
class Model(torch.nn.Module):
    def __init__(self, n: int):
        super().__init__()
        self.linear = torch.nn.Linear(n, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1) - 2  # Apply a linear transformation to the input tensor
        return v1


# Initializing the model
m = Model(8)

