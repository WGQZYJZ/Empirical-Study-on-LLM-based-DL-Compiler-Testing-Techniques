
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + torch.randn(8)  # Add noise to the output of the linear transformation
        return v2


# Initializing the model
m = Model()
