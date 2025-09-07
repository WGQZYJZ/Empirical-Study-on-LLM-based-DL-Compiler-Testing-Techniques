
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(2, 3)
 
    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = v1 - other_tensor  # Subtract 'other' from the output of the linear transformation
        return v2


# Initializing the model