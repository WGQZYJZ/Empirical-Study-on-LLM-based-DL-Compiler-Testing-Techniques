
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - torch.ones_like(v1) # subtracts a tensor of ones
        v3  = F.relu(v2) # Applies the ReLU function to the result
        return v3


# Initializing the model
m  = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

