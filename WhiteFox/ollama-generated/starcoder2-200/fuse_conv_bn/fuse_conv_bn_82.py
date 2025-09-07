
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         return torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)


# Initializing the model 
m = Model() 

# Inputs to the model 
x2  = torch.randn(20, 3)
x1  = torch.randn(4, 3, 5)

__output__  = m(x2)

