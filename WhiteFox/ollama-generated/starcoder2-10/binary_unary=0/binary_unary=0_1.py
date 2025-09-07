
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other
        v3  = F.relu(v2)
        return v3

# Initializing the model with different weights than the previous one and 0 initialization of new parameter 'other' in the layer
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
m(x1)



