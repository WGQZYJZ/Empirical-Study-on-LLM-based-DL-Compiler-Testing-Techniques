
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1, other):
        v1  = self.conv(x1) + other # Add another tensor to the output of a pointwise convolution with kernel size 1 and stride 1
        return v1

# Initializing the model
m  = Model()

