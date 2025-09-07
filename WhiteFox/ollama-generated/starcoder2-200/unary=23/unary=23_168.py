
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 7)
        self.conv2 = torch.nn.ConvTranspose2d(
            8, 3, kernel_size=(7 + 1))
 
    def forward(self, x):

        v1 = self.conv1(x)
        v4 = self.conv2(v1)
 
        return v4
