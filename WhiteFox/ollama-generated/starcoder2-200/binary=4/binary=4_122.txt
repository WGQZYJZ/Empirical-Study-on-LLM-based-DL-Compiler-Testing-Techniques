
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = torch.nn.Linear(32768000, 450)
 
    def forward(self, x1):
        v1 = self.lin1(x1)
        v2 = v1 + other_tensor
        return v2


# Initializing the model with a new tensor as argument to the torch.nn.Linear() constructor:
m  = Model()
other_tensor=torch.randn(1,450)
__output__   = m(x1)
