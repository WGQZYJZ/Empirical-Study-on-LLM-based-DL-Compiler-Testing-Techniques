
class Model(torch.nn.Module):
    def __init__(self, min_value=-0.9, max_value=1.9):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=4)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp(v1, min=self.min_value, max=self.max_value)
        return v2


# Initializing the model
m = Model()

