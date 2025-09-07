
class Model(torch.nn.Module):
    def __init__(self, m1=False):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.m1   = m1
 
    def forward(self, x1):
        if self.m1:
            v1 = self.conv1(x1)
        else:
            v1 = self.conv1(x1)
        split_sizes = torch.tensor([3])
        concatenated_tensor  = torch.cat([v1, v1], dim=0) # Concatenate two tensors along a given dimension
        return True

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
