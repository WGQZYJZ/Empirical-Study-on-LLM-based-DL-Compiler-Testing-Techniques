
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channels=3, out_channels=10, kernel_size=(3,)) # Conv2d is used instead of Conv1d and Conv3d

    def forward(self, x):
        v  = self.conv(x)
        return v

model = Model()
input_tensor = torch.randn((64, 3, 8))
output = model(input_tensor)
