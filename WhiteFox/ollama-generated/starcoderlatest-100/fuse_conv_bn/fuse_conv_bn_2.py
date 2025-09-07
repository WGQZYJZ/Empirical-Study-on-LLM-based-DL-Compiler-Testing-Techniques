 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(2, 2, 3)
        self.bn = torch.nn.BatchNorm2d(2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.conv2d(v1, self.conv.weight, (3, 3), (1, 1)) # Apply convolution with stride and padding to the permuted tensor 
        v3 = torch.nn.functional.batch_norm(v2, v1.shape[-1], eps=0.001) # Use batch norm over 3 dimensions, eps is used for numerical stability
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2, 2)
