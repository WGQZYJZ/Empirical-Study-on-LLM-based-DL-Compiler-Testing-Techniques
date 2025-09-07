
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.Linear(784, 50)(x1)
        v2  = (v1 > 0).float()
        v3  = v1 * negative_slope
        return torch.where(v2, v1, v3)

 # Initializing the model
m = Model()
 
 # Inputs to the model
x1 = torch.randn(64, 784)
 
