
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1  = torch.nn.ConvTranspose2d(3, 8, 7)

    def forward(self, x1):
        v1  = self.conv1(x1)
        v2  = F.relu(v1)
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model