
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.empty([7])
        v4  = self._other()
 
        v1  = self.conv(x1) - v2 
        v3  = relu(v1 + v4)  
        return v3

    @property
    def _other(self):
        return torch.Tensor([0.5])

    def _compute(func_name, value):
         return eval(func_name)(value)

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) 
 
# The expected outputs of the model
__output__  = m(x1)

