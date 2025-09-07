
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv(x1)  # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = torch.matmul(v1, x2).div(0.7071067811865476)  # Multiply the output of the convolution by 0.7071067811865476
        v3 = self.conv(x1) * torch.tanh(v2) + 1  # Apply a sigmoid to the output of the error function
        v4 = torch.matmul(v3, x2).div(0.7071067811865476) * torch.exp(v2 - 1)  # Multiply the output of the convolution by 0.7071067811865476 + 1
        return v4


# Initializing the model
m = Model()


