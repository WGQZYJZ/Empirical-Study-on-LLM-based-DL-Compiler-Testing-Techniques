
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=5)

    def forward(self, x):
        out = self.conv1(x) # [N][C][H][W]
        out += torch.randn((out.shape)) # Broadcast the tensor (requires `out.shape`)
        out = torch.relu(out)
        return out

# Initializing the model
m  = Model()

