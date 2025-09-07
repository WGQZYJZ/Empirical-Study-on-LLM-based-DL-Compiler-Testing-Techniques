
class Model(torch.nn.Module):
    def __init__(self, num_splits):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) # split the input tensor into several tensors along a given dimension
        v2 = torch.cat([v1[i] for i in range(num_splits)], dim=1)  # concatenate them back
        return v2


# Initializing the model with a fixed number of splits
m = Model(4)

