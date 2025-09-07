
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = torch.nn.Linear(10, 5)
 
    def forward(self, x1): 
        return self.layer(x1)


# Initializing the model
m = Model()

# Input to the model
x1  = torch.randn(32, 10)
 
# Outputs from the model
__output__  = m(x1)