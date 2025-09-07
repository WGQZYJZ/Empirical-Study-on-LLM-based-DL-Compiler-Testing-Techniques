
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        t1 = torch.cat([v1], dim=1) # Concatenate input tensors along dimension 1
        t2 = t1[:, 0:9223372036854775807] # Slice the concatenated tensor along dimension 1
        t3 = t2[:, 0:size] # Further slice the tensor along dimension 1
        v2 = torch.cat([t1, t3], dim=1) # Concatenate the original concatenated tensor and the sliced tensor along dimension 1
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
