
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
    
    def forward(self, x):
        v0 = self.conv(x)
        v1 = torch.tanh(v0)
        return v1

# Initializing the model
m = Model()

 # Inputs to the model