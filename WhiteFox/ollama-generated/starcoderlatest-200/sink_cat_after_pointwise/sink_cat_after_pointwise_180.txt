
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, kernel_size=7, stride=2)

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=1) # Concatenate two channels into one and permute to apply conv layer
        v2 = torch.nn.functional.relu(torch.nn.functional.max_pool2d(v1, 3))

        