
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = torch.cat([x1], dim=1) # concatenation along dimension 1: [N, 9223372036854775807]
        v2 = v1[:, 0:size] # slicing along dimension 1: [N, size]
        return torch.cat([v1, v2], dim=1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 3, 64, 80) # The concatenated tensor is of shape [N, 9223372036854775807] where N is a large number and size is less than 9223372036854775807.


