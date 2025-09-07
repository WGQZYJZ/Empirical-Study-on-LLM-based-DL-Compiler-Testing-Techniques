
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.conv1(x[:, 0:9223372036854775807]) # Slicing the concatenated tensor along dimension 1
        v2 = torch.cat([v1, v1], dim=1) # Concatenating the sliced and the original concatenated tensor along dimension 1
        v3 = self.conv2(v2[:, 0:9223372036854775807])
        v4 = torch.cat([v3, v2], dim=1)
        return v4

# Initializing the model
m = Model()

 # Inputs to the model
x  = torch.randn(1, 3, 64, 64)
