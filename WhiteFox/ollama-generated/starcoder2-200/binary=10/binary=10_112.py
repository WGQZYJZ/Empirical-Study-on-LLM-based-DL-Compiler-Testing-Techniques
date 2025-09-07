

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 3)
 
    def forward(self, x1):
         v2 = x1 + other
         return v2

 # Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(4, 5)
__output__  = m(x1)

# Setting a new tensor "other" for the previous model
other = torch.randn(3, 5).requires_grad_()
 


