
class Model(torch.nn.Module):
    def __init__(self, d1: int, d2: int):
        super().__init__()
        self.linear = torch.nn.Linear(d1, d2)
 
    def forward(self, x1):
        v1 = self.linear(x1)  # Apply linear operation to the input tensor
        v2 = torch.cat([v1, v1], dim=1)  # Concatenate along dimension 1
        return v2


# Initializing the model
m = Model(3, 8)

# Inputs to the model
x1 = torch.randn(4, 3)
