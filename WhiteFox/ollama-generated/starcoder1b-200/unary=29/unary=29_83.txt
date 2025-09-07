
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=3, stride=1, padding=1)
 
    def forward(self, x1, min_value=0, max_value=255):
        v1 = self.conv(x1, min_value, max_value)
        return v1


# Initializing the model
m = Model()

