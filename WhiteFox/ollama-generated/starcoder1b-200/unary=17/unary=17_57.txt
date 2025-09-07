
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        return self.relu(self.conv_transpose(x1))
 
    def relu(self, x):
        return F.relu(x)


# Initializing the model
m = Model()

