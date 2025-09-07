

class Model(torch.nn.Module):
    def __init__(self, d1 = 50, d2 = 30, d3=64, d4=8):
        super().__init__()
        
        self.d1 = torch.nn.Linear(d1, d2)
        self.d2 = torch.nn.Conv2d(d2, d3, (3, 3), padding='same')
        self.d3 = torch.nn.MaxPool2d((3, 3))
        self.d4 = torch.nn.Conv2d(d3, d4, (50 - d3 - 1 + 1) // 2 + 1, stride=1, padding='same')
 
    def forward(self, x):
        
        v1 = F.relu(self.d1(x))
        v2 = self.d2(v1)
        v3 = self.d3(v2) 
        v4 = self.d4(v3).sum(dim=0) 
        return v4


# Initializing the model 
m = Model() 

# Inputs to the model 
x = torch.randn((1, 50)) 

# Outputs from the model
__output__  = m(x)

