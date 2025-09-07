
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.linear(x1) + other_tensor
        return v1

 # Initializing the model
m  = Model()
 
 # Inputs to the model
x1  = torch.randn(20, 3, 64, 64)
other_tensor  = torch.randn(20,)
 
__output__  = m(x1)

