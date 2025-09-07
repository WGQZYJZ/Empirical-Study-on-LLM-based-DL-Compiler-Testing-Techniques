
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, kernel_size=7, padding=3)

    def forward(self, x):
        x = torch.nn.functional.pad(x, (1, 1)) 
        return torch.nn.functional.relu_(self.conv1(x))

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.rand(4096, 32)

