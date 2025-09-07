
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v0 = x1 - v1 # Subtract the output of the convolution from another tensor
        v1 = conv(x1)
        v2 = relu(v0)
        return v2


# Initializing the model and inputs to the model. The model should be different from that above.
m  = Model()
x1 = torch.randn(1, 3, 64, 64)
