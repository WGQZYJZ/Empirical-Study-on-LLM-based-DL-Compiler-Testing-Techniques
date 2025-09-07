
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 9, 1)
        self.linear1 = torch.nn.Linear(1048576, 8)
 
    def forward(self, x):
         v1 = self.conv1(x)
         v2 = v1 + other_tensor
         v3 = torch.relu(v2)
         v4 = self.linear1(torch.flatten(v3))
         return v4


# Initializing the model
m  = Model2() 

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
other_tensor = torch.ones((1, 9, 80*80), dtype=torch.float)

__output__  = m(x)

