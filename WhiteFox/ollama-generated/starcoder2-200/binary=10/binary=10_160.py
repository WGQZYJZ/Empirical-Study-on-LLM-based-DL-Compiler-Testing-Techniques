
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + torch.randn(v1.size())
        return v2


# Initializing the model and generating an input tensor that is not used in previous model
m  = Model()
x1  = torch.randn(4, 5, 6)
 

# Inputs to the model
x1  = torch.randn(100, 32)
__output__  = m(x1)

