
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
    
    def forward(self, x1):
        v1 = linear(x1)
        v2 = torch.clamp_min(v1, min=-50) # min is -50 
        v4 = torch.clamp_max(v2, max=10)  # max is 10
        return v4


# Initializing the model
m  = Model()
__output__  = m(x1)
 
