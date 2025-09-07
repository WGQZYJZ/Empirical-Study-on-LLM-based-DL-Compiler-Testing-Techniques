
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
        self.relu   = torch.nn.ReLU()
 
    def forward(self, x2):
       v100 = self.conv(x2)
       return self.relu(v100)

# Initializing the model
m2  = Model2()

 # Inputs to the model
 x2  = torch.randn(4, 3, 64, 64)
__output__  = m2(x2)
