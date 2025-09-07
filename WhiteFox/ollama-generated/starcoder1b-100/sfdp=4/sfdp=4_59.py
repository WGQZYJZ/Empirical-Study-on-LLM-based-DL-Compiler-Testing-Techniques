
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)

    def forward(self, x):
        # Apply pointwise convolution with kernel size 1 to the input tensor
        v = self.conv1(x)
        v = v * 0.5

        # Multiply the output of the convolution by 0.7071067811865476
        w = torch.tanh(self.conv2(v))
        
        # Apply a pointwise linear transformation to the result of a convolution
        return torch.sum(w, dim=0)


# Initializing the model
m = Model()

