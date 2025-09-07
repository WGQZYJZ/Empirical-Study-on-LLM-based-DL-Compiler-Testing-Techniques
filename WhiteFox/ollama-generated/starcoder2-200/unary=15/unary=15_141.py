
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = F.relu(v1) # You can also write: F.relu_(v1), this modifies the existing input in-place.
        return v2


# Initializing the model
m  = Model()
 
 # Inputs to the model
 x1  = torch.randn(1, 3, 64, 64)
  __output__  = m(x1)

# Finalized model 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1): # You can also write: F.relu_(x), this modifies the existing input in-place.
        v1  = self.conv(x1) 
        return torch.nn.functional.relu(v1, inplace=False)
 
 
 # Inputs to the model
 x1  = torch.randn(1, 3, 64, 64) 
 __output__  = m(x1)
