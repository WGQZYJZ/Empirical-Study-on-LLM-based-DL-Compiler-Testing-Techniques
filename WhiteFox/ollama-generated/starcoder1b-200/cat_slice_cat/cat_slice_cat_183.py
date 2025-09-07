
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1, x2)
        v2 = v1[:, :, :, :]  # Further slice the tensor along dimension 1
        v3 = v2[:, :, :size]  # Further slice the tensor along dimension 1
        v4 = torch.cat([v1, v3], dim=1)  # Concatenate the original concatenated tensor and the sliced tensor along dimension 1
        return v4


# Initializing the model
m = Model()

