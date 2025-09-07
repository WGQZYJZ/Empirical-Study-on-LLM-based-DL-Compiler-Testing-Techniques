
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1d = torch.nn.ConvTranspose2d(3, 8, kernel_size=7)
 
    def forward(self, x1):
        v1 = self.conv1d(x1)
        v2 = torch.relu(v1)
        return v2


m  = Model()

# Initializing the model