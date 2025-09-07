
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 16, kernel_size=4)

    def forward(self, x):
        return torch.nn.functional.batch_norm(x, self.conv(x))

# Initializing the model