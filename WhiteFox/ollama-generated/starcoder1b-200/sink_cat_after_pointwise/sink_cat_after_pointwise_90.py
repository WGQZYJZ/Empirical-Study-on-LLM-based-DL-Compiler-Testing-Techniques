
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1  = torch.cat([x1, x1], dim=0) # Concatenate two inputs
        v2  = torch.relu(v1)               # Apply ReLU to the concatenated input
        return v2


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
