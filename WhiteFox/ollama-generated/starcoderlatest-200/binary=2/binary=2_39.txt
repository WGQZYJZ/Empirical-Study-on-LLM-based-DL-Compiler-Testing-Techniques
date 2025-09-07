
class Model2(torch.nn.Module):
    def __init__(self, other: torch.Tensor):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        return v6


# Initializing the model with different inputs for each scenario and storing them in a tuple variable
m2_1 = Model(torch.zeros((3, 64, 64))) # Scenario where 'other' is an empty tensor
m2_2 = Model(torch.randn((3, 64, 64))) # Scenario where 'other' is a random tensor of the same shape as output
