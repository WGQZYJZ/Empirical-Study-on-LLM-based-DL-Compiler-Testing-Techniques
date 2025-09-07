
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, kernel_size=2, stride=1, padding=0)
        self.relu = torch.nn.ReLU()
        self.sigmoid = torch.nn.Sigmoid()
 
    def forward(self, x):
        v1 = self.conv_transpose(x)
        v2 = self.relu(v1)
        v3 = self.sigmoid(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(1, 8, 50, 50)
