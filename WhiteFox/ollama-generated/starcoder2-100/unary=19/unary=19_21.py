
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         return torch.sigmoid(
            self.lin = torch.nn.Linear(32*64*64, 8)
        )


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(10, 32*64*64)
__output__  = m(x1)

