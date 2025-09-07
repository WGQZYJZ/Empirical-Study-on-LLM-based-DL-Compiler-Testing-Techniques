
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(512 * 7* 7, 4096)
        self.sigmoid  = torch.nn.Sigmoid()
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = self.sigmoid(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m = Model()
 
# Inputs to the model 
x1 = torch.randn(8, 512*7*7)  # The shape of x is 8, 4096 in this case 
 __output__  = m(x1)
 
