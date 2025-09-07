
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1):
       v  = torch.split(input1, [48]) 
       return torch.cat([v[i] for i in range(len(v))], -3)

# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(96*270*5*1) 

__output__  = m(torch.reshape(x, (96, 270, 5, 1)))

