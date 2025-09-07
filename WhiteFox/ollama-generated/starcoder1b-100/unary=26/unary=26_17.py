
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1)
        # Use ConvTranspose2d to do a pointwise transpose convolution on 8-dimensional input tensor and then apply ReLU operation on the output

    def forward(self, x):
        v = self.conv_transpose(x) > 0
        return torch.relu(v)


# Initializing the model
m = Model()


