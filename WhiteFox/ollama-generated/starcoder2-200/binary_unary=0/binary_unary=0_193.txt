

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) + other
        v2  = F.relu(v1)
        return v2


# Initializing the model
m  = Model()
other  = torch.randn(3,8,64,64) # This is another input tensor of the same shape and size as v1
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)


