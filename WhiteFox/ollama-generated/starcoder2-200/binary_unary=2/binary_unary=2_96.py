
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other
        v3  = torch.relu(v2) # this line should be removed
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
 
# Define the output of the convolution layer in the forward method before relu call
v2  = m.conv(x1) - other # this line should be removed 
 
# Inputs to the model for test 5.
test_inputs = [
    [torch.randn(3, 640, 80), torch.rand(80).mul_(9)],
    [torch.randn(7, 213, 44), 0], # this line should be removed
    [torch.randn(5, 713, 13), None]
]

