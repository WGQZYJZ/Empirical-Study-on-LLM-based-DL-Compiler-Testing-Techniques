
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, **kwargs): 
        v2  = kwargs["other"]
        v3  = self._linear(x1)
        v4  = v3 + v2
        v5  = torch.relu(v4)
#         print(v4)
        return v5
 
    def _linear(self, x):
        v1 = torch.nn.Linear(8 * 64 ** 2 , 9)(x) 
        return v1


# Initializing the model
m = Model()
 

x1 = torch.randn(3072, requires_grad=True)
other = torch.randn(9, requires_grad=True)
 
    
__output__  = m(x1, other=other)
 

