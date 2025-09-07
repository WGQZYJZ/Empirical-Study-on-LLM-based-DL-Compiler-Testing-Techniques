
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)  # First split the input tensor into 3 and 4 tensors
        v2 = torch.split(v1, [5], dim=1)[0]  # Apply a single split to get two new tensors: [v2, v3]
        v3 = torch.split(v1, [5, 6], dim=2)  # Two consecutive splits on dimensions of each tensor (1st dimension is the same for both tensors, so no need to specify dim).
        v4 = torch.cat([torch.split(t1, [5], dim=0) for t1 in v3])  # Split every dimension into a single tensor
        return v4


# Initializing the model
m = Model()


