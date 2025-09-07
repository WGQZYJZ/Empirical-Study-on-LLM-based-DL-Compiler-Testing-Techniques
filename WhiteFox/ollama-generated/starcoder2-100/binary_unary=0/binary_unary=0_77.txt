
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other # Add another tensor to the output of the convolution
        v3  = torch.relu(v2)
        return v3


# Initializing model
m = Model()

# Inputs for the model
x1  = torch.randn(1, 3, 64, 64)
