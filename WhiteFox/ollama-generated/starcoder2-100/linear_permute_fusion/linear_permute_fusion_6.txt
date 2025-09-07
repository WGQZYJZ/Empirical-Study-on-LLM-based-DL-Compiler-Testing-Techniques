
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.nn.functional.linear(x1, self.linear2.weight, self.linear2.bias)
        v4  = torch.nn.functional.linear(v3, self.linear1.weight, self.linear1.bias) 
        return v4

# Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(2, 8)

 
__output__= m(x1)
