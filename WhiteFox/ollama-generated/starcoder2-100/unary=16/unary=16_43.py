
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = torch.relu(v1)
        return v2

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(3000, 10)
__output__  = m(x1)

System: [ERROR] Invalid PyTorch code detected (see above error messages). Please fix and run the test again

