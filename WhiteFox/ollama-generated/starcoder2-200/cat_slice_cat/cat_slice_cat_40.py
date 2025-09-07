
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v4 = self.__output__[:, :, :9223372036854775807]
        return torch.sum([x1, v4], dim=1).permute(0, 3, 2)

# Initializing the model
m = Model()

