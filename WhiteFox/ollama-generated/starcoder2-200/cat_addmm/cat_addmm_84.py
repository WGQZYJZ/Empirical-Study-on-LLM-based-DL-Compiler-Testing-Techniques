

# Initializing the model with torch.nn.Sequential() 
m1 = torch.nn.Sequential(
    torch.nn.Linear(6, 6),
    torch.nn.Tanh(),
)

# Initializing the model with torch.nn.ModuleList()
class Model():
    def __init__(self):
        self.net1  = torch.nn.Linear(2048, 3)
        self.conv2d = torch.nn.Conv2d(6, 6, 1)
 
    def forward(self, x):
        x2  = m1(x) + self.conv2d(x)
        return x2
m2 = Model()
__output__  = m2(torch.zeros(32, 4096))

