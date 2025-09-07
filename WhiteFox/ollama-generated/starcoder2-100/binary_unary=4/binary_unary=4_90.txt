
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(8, 10)

 # Applying the model with keywords arguments on the model and on the input tensor
__output__  = m(x1), m.__call__(x1, other=torch.zeros_like(v2))
