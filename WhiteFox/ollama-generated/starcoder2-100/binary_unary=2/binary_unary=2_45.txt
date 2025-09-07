
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other
        v4  = torch.relu(v2)
        return v4

# Initializing the model with an input tensor that is different from the previous one.
other  = torch.randn_like(x1, dtype=torch.float64)
m  = Model()

 # Inputs to the model 
 x1  = other + torch.randn(1, 3, 64, 64)
 
