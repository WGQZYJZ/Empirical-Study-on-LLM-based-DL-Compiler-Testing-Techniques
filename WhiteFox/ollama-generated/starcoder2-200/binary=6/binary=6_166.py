
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 - 0.5 # Subtracting a constant value from the output of linear transformation
        return v2


# Initializing the model