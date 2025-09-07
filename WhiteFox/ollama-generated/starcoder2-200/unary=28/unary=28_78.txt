
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(20,1)
 
    def forward(self, x1):
         v1 = self.linear(x1)
         v3 = torch.clamp_min(v1, -5) # This example uses keyword arguments in the clamp method to specify a minimum value of `-5` as an argument.
         return  v2


# Initializing the model
m  = Model()

# Inputs to the model:
x1  = torch.randn(30, 20)
__output__  = m(x1)

