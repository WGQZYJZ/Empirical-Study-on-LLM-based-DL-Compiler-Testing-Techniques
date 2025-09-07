
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3,1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.tanh(v1) # Replace the line below with: v2 = torch.abs(v1)
        return v2


# Initializing and using the model
m  = Model()
__output__  = m(torch.randn(3, ))
