
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = v1 + other 
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m = Model()
other = torch.randn(10).requires_grad_()

 # Inputs to the model
x1 = torch.randn(64, 32)
 
# Output of the model: output should be different from __output__
__output__  = m(x1)
