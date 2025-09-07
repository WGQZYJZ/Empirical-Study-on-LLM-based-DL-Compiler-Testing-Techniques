
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.addmm(v1, m1, m2)
        v3 = torch.cat([v2], dim=1)  # Concatenate the result along a specified dimension. By default this operation is done between the second and third dimensions.
        return v3
