
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        # Concatenate the result tensor along a specified dimension
        v1 = self.conv(torch.cat([x1, x1, x1, ..., x1], dim=-1))
        v2 = torch.cat([v1, v1, v1, ..., v1], dim=-1)
        return v2


# Initializing the model
m = Model()

