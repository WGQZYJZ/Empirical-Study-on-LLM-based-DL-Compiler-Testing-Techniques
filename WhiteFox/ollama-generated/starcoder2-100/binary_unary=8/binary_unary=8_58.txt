
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.v  = Parameter(tensor = torch.Tensor([5]))
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + self.v
        v3  = torch.relu(v2) # Use ReLU to make the value non-negative
        return v3


# Initializing the model