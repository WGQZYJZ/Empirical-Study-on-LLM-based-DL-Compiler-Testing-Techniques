
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3072,10)
 
    def forward(self, x1):
         v1  = self.linear(x1) 
         v2  = v1 + self._other_tensor # this will be different from the previous one!
         return v2

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5,3072)
_other_tensor = 0.6*torch.rand(4,8)-0.1 # this will be different from the previous one! 


__output__  = m(x1)

