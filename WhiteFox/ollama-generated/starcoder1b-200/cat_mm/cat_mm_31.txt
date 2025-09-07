
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.cat([v1, v1, ..., v1], dim=0)  # Concatenate the result along dimension 0 (batch-wise)
        return v2


# Initializing the model
m = Model()


