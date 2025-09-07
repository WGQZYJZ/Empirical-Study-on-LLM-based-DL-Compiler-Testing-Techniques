
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8*64**2, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v3 = v1 + __other__
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 8*64**2)

 # Initialization of another tensor with the same shape and data type as the output of a linear transformation (which is not defined by __other__). In practice, you could generate it by using `other = torch.zeros_like(v3)`.
__other__  = other
 
 # Model's output
__output__  = m(x1)

 