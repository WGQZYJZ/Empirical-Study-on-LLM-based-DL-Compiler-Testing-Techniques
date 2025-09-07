
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.split(x1, split_sizes=(x1.shape[0],), dim=0)[0]
        v2 = self.conv(v1)
        return v2


# Description of requirements
There is no model restrictions for this pattern to be valid since we cannot determine whether the input tensor should have a particular shape and dimension along which it was split. 

# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.split(x1, split_sizes=(x1.shape[0],), dim=0)[0]
        v2 = torch.cat([v1 for i in range(x1.shape[0])], dim=0) 
        return self.conv(v2)

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 64, 64)
