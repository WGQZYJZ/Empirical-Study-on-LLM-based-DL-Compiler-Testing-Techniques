
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(30,2)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        return v1
 
# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(4, 30)

 # Other argument for torch.nn.Linear: other=torch.zeros_like(x1) 
__output__  = m(x1)

