
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(49, 1)
 
    def forward(self, x1):
        v2 = torch.sigmoid(x1 @ torch.zeros((1, 4)))
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(50, 49)
__output__  = m(x1)

