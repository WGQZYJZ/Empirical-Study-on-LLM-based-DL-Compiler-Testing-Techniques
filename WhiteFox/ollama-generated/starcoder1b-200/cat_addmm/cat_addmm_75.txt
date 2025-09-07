
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 3, stride=2, padding=0)
 
    def forward(self, x):
        v = torch.addmm(
            self.conv1(x),  # First convolution
            torch.transpose(
                self.conv2(
                    x),  # Second convolution
                2))  # Perform a matrix multiplication of the first and second convolution
        return v


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(2, 8, 3, 3)
