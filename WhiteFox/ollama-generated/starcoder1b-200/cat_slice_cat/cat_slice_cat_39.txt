
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2):
        # Concatenate x1 and x2 along dimension 1
        v1 = torch.cat([x1, x2], dim=1)
 
        # Take the slice along dimension 1 and then further take a slice along dimension 1
        v2 = v1[:, :5]  # Slice along dimension 1 with index 0 to 4
        v3 = v2[:, :5]   # Further slice along dimension 1 with index 0 to 4
 
        # Concatenate the original concatenated tensor and the sliced tensor along dimension 1
        v4 = torch.cat([v1, v3], dim=1)
 
        return v4


# Initializing the model
m = Model()


