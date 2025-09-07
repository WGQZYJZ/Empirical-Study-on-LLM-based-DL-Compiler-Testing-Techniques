
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784,10)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2 = v1 + self._other_tensor
 
        return v2


m  = Model2()
 
__output__  = m(_input_)

# Initializing the model
m = Model2()

# Inputs to the model
_input_ = torch.randn(64,784)
__other_tensor__ = torch.randn(64,10) # A randomly generated tensor that will be added later

