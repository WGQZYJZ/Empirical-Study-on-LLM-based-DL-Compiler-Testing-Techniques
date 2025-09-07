
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, **kwargs):
        v1  = torch.nn.functional.linear(x1, kwargs['other']) 
        v2  = v1 + self._v3
        v3  = torch.nn.functional.relu(v2)
        return v3
        
# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(5, 4)
other = torch.randn(4)
m.__output__  = m(x1, other=other)

