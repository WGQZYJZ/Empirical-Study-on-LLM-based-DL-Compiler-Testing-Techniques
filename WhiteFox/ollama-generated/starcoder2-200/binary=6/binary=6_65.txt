
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 4)
 
    def forward(self, x2):
        v7 = torch.randn(5).requires_grad_(True) # Generate a tensor for linear transformation that is also requiring gradients
        v8 = self.linear(x2)
        v9 = v8 - v7
        return v9

# Initializing the model
n  = 100
m = Model()

