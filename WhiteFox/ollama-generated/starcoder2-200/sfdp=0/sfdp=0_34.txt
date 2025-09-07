
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=5)
        self.conv2 = torch.nn.Conv2d(8, 64, 5)
 
    def forward(self, x1):
         v1  = F.relu_(F.max_pool2d(x1))
         v2  = F.relu_(F.max_pool2d(v1))
         return torch.cat([
             self.conv1(x1),
             self.conv2(v2)], dim=1)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3, 8, 640, 640).float().requires_grad_(True) # The input to the model must have floating point data type and should be a tensor with 5 channels (RGB), of size [3, 8, 256, 256]
