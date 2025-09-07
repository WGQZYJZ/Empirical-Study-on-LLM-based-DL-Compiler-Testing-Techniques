
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        return torch.tanh(v1)


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 32*784) # 32 is a hyperparameter. Use a larger value when testing for production.
__output__  = m(x1)

