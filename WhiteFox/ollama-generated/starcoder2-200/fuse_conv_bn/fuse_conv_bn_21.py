

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # x1 is 3D.
        v = torch.nn.functional.conv2d(x1, torch.nn.functional.conv2d(0).weight)

# Initializing the model