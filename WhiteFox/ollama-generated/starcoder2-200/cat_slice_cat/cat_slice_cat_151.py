
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = x1[:, 0:9223372036854775807] # Slicing the tensor along dimension 1
        v2 = self.conv(v1) # Apply a pointwise convolution to the sliced input tensors
        v3 = torch.cat([x1, v2], dim=1) # Concatenate the original concatenated tensor and the sliced tensor along dimension 1

        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(50, 3, 64, 64)
