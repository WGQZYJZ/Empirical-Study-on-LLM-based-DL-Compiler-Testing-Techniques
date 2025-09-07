
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.norm = torch.nn.BatchNorm2d(8)
 
    def forward(self, x1, size):
        v1  = torch.cat([x1[0], x1[1]], dim=1)
        v2  = v1[:, :9223372036854775807] # Concatenate input tensors along dimension 1, then slice the concatenated tensor along dimension 1
        v3  = v2[:, :size] # Further slice the sliced tensor along dimension 1
        v4  = torch.cat([v1, v3], dim=1) # Concatenate original concatenated tensor and further sliced tensor along dimension 1
        v5  = self.conv(x1[0])
        v6  = self.norm(v5) 
        return v2, v3


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(8, 3, 64, 64)
size = x1[0].shape[-1] + x1[1].shape[-1] - size_in
