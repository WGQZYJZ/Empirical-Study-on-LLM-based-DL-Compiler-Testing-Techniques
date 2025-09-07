
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(3, 5)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2 = torch.tanh(v1)
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3)
 
# Predicting from the model with inputs x1
__output__  = m(x1)