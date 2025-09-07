
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = Conv2d_input_size_3
        self.conv2 = Conv2d_input_size_4

    def forward(self, x1, x2, x3, x4):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)  # Conjugate transpose of the input tensor with the output of the convolution
        v3 = torch.cat([v1, v1, v1, v1], 0) # Concatenation of the result tensors along 0
        return v2


# Initializing the model
m = Model()


