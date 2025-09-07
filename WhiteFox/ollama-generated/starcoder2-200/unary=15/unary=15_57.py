
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v0  = F.relu(self.conv(x1))
        return v0

# Initializing the model with randomly initialized parameters:
m = Model2()

