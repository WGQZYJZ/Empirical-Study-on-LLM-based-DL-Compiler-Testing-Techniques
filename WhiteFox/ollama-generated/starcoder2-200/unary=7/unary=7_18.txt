
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 8, bias=False)
 
    def forward(self, x1):
        v1 = self.linear(x1) 
        v2 = v1 * clamp(min=0., max=6.)   
        v3 = (v2 + 3.).clamp_(min=0).div_(6) # NOTE: The clamp_ is used as the output of the linear transformation is divided by `6`
        return v3

# Initializing the model
m = Model()

# Input to the model
x1 = torch.randn(25, 8, requires_grad=True)

 # Compute forward and backward passes
yhat = m(x1) 

 