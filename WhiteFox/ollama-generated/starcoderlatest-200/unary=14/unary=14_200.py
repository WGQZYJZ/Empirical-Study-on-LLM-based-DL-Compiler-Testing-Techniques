
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.Conv2d(16, 3, kernel_size=(5, 5), stride=4, padding=2)
        self.sigmoid = torch.nn.Sigmoid()
 
    def forward(self, x1):
        v1 = self.conv_t(x1)
        v2 = self.sigmoid(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 16, 480, 672)
