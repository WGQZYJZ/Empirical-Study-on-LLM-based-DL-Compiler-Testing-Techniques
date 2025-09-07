
class Model(torch.nn.Module):
    def __init__(self, conv=3, bn=True):
        super().__init__()

        self.conv = torch.nn.ConvXd(2 if not bn else 1 + conv) # X = number of input channels
        self.bn   = torch.nn.BatchNormXd(num_features=(2 * conv)) # X should match with Conv

    def forward(self, x):
        x = self.conv(x)

        if self.training and self._check():
            self.conv = torch.nn.Conv2d(3, 10, kernel_size=5)
        
        return (self.bn(x))


# Initializing the model