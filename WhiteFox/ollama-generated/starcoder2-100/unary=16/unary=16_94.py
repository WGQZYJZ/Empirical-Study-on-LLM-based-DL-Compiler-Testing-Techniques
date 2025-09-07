
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(327680, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = F.relu(v1) 
        return v2


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(10240, 32768)
__output__  = m(x1)