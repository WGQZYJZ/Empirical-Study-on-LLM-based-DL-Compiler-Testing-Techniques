
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 2)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.tanh(v1) 
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(30,)



# Initializing an optimizer for the model parameters in the first module, and the second module of the first sub-module of the main module. We assume that the second module of the first sub-module is connected with the third layer (second and third layers are shared).
import torch

m  = torch.nn.Sequential(
    torch.nn.Linear(20, 15), 
    torch.nn.ModuleList([
        torch.nn.Sequential(
            torch.nn.Linear(30, 40), 
            torch.nn.Linear(40, 8)
        )
    ]))

torch_optimizers = [
   torch.optim.SGD(m[0].parameters(), lr=1e-3,), 
   torch.optim.Adam(list(m[1][0][2:].parameters()), lr=1e-4),  
   # The third to the last layer of m[1][0] is connected with the first layer in m[1][1].
]

