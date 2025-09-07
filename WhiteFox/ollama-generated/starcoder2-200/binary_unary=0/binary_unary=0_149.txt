
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1  = self.conv(x1) # Pointwise convolution with kernel size 1 on the input tensor
        v2  = v1 + torch.randn((v1.size()[0], v1.size()[1]))
        v3  = F.relu(v2)   # ReLU activation function applied to result after adding another tensor

        return v3

# Initializing the model
m  = Model()


# Inputs to the model:
x1 = torch.randn(1, 3, 64, 64)
