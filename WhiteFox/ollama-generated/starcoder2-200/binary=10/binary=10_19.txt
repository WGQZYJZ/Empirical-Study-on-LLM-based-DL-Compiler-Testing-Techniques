
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(10, 8)
 
    def forward(self, x1, other=None):
        v1  = self.lin(x1)
        if other is not None:
            v2 = v1 + other
        return v2

# Initializing the model with the custom tensor `other` in the forward method
m  = Model()

 # Inputs to the model for this example scenario (you can choose different inputs that work)
x1  = torch.randn(3, 50, 8)

