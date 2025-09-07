
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         v1 = torch.nn.functional.dropout(x1, p=0.5)
         v2 = torch.rand_like(v1, 3.14)

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 3)
 
# Outputs from the model on inputs x1 and x1^2
__output__1 = m(x1)
__output__2 = m((x1*x1))
 
