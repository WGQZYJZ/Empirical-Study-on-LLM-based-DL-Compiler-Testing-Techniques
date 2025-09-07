
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0):
        t2  = torch.cumsum(x0, dim=1)
        return t2

 # Initializing the model
  m  = Model()

 
# Inputs to the model
input_shape = (16,)
dtype = 'float32'
layout  = None
device = 'cpu'

x0 = torch.empty(input_shape, dtype=dtype, layout=layout, device=device)

 