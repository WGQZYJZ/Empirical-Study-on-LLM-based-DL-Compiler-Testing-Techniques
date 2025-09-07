
class Model(torch.nn.Module):
    def __init__(self, other1 = torch.ones([3]), other2 = torch.zeros([])):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = v1 + other1 
        return v2


# Initializing the model
m  = Model()
other1 = torch.ones([3]) # Tensor to be added as a keyword argument in the forward pass of the model. It is different from the tensor passed in the initializtion of m (which is torch.zeros([]))

