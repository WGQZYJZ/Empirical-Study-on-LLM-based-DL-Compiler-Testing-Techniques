
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(10, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        # Multiply the input tensors with each other and then concatenate them along the second dimension of both inputs
        v1 = self.conv(x1).unsqueeze(1).unsqueeze(-1) * self.conv(x2).unsqueeze(-1)
        v2 = v1 + 1
        v3 = torch.cat([v1, v2], dim=-1)
        return v3


# Initializing the model
m = Model()


