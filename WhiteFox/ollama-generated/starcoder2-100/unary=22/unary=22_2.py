
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.linear = torch.nn.Linear(7*7*8, 49)
 
    def forward(self, x1):
        v1 = self.conv(x1)
 
        v2 = self.linear(v1.view(-1)) 
        v3 = torch.tanh(v2)
        return v3
 
m  = Model()
# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
 
