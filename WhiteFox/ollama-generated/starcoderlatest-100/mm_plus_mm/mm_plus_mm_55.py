
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 5)
        self.conv2 = torch.nn.Conv2d(6, 6, 5)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
input1 = torch.randn(1, 3, 64, 64) # input tensor of shape (N, C1, H, W) for one batch data set
input2 = torch.randn(1, 3, 64, 64) # input tensor of shape (N, C2, H, W) for another batch data set
