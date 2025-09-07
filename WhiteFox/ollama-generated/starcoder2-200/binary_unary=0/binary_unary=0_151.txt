
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) + 0 # Replace this with the other tensor in the convolution pattern
        v2 = torch.relu(v1)
        return v2
