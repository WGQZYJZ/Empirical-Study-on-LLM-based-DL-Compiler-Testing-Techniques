
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1).view(-1, 8 * 1 * 1)  # Reshape x1 to (N, 8*H*W)
        v2 = torch.cat([v1, x2], dim=1)        # Append the input tensor x2 to each column of v1 as a new dimension 1
        return v2


# Initializing the model
m = Model()


