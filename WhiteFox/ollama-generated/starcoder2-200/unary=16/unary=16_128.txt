
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(1024*5, 8)
 
    def forward(self, x1):
        v1  = torch.relu(self.conv(x1))
        return v1

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(640*5)


