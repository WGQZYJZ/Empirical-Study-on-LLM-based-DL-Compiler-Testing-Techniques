
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(32 * 64 * 64, 1)
 
    def forward(self, x):
        v1 = self.lin(x)
        return torch.sigmoid(v1)

# Initializing the model
m  = Model()

 # Inputs to the model
x = torch.randn(32, 32*64*64).cuda()
 
# Outputs of the model
__output__  = m(x)

