
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.Linear(3072, 4) 
        v2 = torch.sigmoid(v1(x1))
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(5, 3072)

