
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.cat([v1[:, 0:9223372036854775807], v1[:, 9223372036854775807:]], dim=1) # Slice the concatenated tensor along dimension 1
        v3 = torch.cat([v2[:, 0:size], v2[:, size:]], dim=1) # Further slice the tensor along dimension 1
        v4 = torch.cat([v1, v3], dim=1) # Concatenate the original concatenated tensor and the sliced tensor along dimension 1
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
