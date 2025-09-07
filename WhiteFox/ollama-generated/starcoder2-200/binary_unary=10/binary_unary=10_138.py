
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         v1  = torch.nn.Linear()(x1)
         v2  = v1 + 56
         v3  = torch.nn.ReLU()
         return v3


# Initializing the model
m  = Model()
# Inputs to the model
x1 = torch.randn(4, 800) 
 