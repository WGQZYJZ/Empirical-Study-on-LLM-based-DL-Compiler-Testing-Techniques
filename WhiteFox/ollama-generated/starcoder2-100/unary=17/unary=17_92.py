
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTranspose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)

    def forward(self, x1):
        v1  = self.convTranspose(x1)
        v2  = F.relu(v1)

        return v2


# Initializing the model