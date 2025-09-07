
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1) # input tensor: 3x64x64
        self.conv2 = torch.nn.Conv2d(8, 16, 1) # input tensor: 8x64x64
 
    def forward(self, x):
        v1 = self.conv1(x) # input tensor: 3x64x64
        v2 = self.conv2(v1) # input tensor: 8x64x64
        return torch.mm(v1, v2) # output of matrix multiplication between two conv layer outputs
 

# Initializing the model
m = Model()


