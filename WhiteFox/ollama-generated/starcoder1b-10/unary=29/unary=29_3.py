
class Model(torch.nn.Module):
    def __init__(self, min_value=1, max_value=20):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1, min_value=1, max_value=20):
        v1 = self.conv(x1, min_value=min_value, max_value=max_value)
        return v1


# Initializing the model
m = Model()


