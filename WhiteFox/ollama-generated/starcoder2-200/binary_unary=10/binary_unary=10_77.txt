
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 10)
 
    def forward(self, x1):
        v2 = torch.relu(x1 + other)
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
other = torch.randn(10).cuda()
x1 = torch.randn(3).cuda()
__output__  = m(x1)

