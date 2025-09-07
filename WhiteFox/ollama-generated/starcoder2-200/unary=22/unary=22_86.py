

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.tanh(v1) 
        return v2


# Initializing the model
m = Model()
 
 # Inputs to the model
x1 = torch.randn(3072, 2048)
  __output__  = m(x1)
 

# The outputs from all tensors
t1 = 6.945541
t2 = -0.27734846


