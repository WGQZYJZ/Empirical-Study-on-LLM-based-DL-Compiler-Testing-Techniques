
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1, padding=0)
        self.relu  = torch.nn.ReLU()
 
    def forward(self, x):
        v_1   = self.conv(x)
        v_2   = self.relu(v_1)
        return v_2

# Initializing the model
m = Model()
 
# Inputs to the model
x  = torch.randn(1,3,64,64)
__output__  = m(x)

