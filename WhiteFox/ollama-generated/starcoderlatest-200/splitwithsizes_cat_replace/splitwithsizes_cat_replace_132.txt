
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [1] * len(x1.size())
        split_sizes[0] *= 2 # Split by splitting along the height dimension first
        v1 = self.conv(x1)
        concatenated_tensor = torch.cat([v1], dim=1)
 
        return True


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64) # Split along the height dimension first
