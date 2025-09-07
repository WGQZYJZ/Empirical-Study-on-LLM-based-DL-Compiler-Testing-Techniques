
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v5  = v1 + self.other
        v6  = torch.relu(v5) 
        return v6


# Initializing the model
m  = Model()
m.other  = torch.randn(3, 8, 32, 32) # Some tensor of the same size and shape as conv1's output


# Inputs to the model
x1  = torch.randn(4, 3, 64, 64)
m.__output__  = m(x1)


