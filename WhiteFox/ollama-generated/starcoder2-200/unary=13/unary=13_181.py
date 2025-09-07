
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32768, 1)
 
    def forward(self, x):
        v0  = F.sigmoid(x) 
        v1  = self.linear(v0 )
        return v1


# Initializing the model
m = Model()

 # Inputs to the model
x = torch.randn(4326897)
__output__= m(x)