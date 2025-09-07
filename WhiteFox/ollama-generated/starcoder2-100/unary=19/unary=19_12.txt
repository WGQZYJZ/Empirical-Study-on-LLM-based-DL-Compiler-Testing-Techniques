

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*4*4 , 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.sigmoid(v1) # Here we want to find a sigmoid-based model, but we do not care about the initial value of the model
        return v2


# Initializing and running the model
m = Model()
output  = m(torch.rand(10,32*4*4))