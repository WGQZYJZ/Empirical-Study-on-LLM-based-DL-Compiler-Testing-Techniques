
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 4, kernel_size=(2,2), stride=(1,1))

    def forward(self, x1):
        y1 = self.conv1(x1)
        return y1

# Initializing the model
m = Model()

 # Inputs to the model
 x1 = torch.randn(3, 1, 2, 4)
 