
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(8 * kdim * kdim, ddim)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        # Apply pointwise convolution with kernel size 1 to the input tensor
        w1 = torch.nn.functional.point_conv2d(v1, weight=weight, stride=1, padding=1, dilation=1)
        v2 = w1 * 0.5
        v3 = w1 * 0.7071067811865476
        v4 = torch.erf(v3)
        # Apply the error function to the output of the convolution
        w2 = torch.nn.functional.point_conv2d(v4, weight=weight, stride=1, padding=1, dilation=1)
        v5 = w2 + 1
        v6 = v2 * v5
        # Apply dropout to the softmax output
        dropout = torch.nn.functional.dropout(v6, p=dropout_p)
        return self.linear(dropout)


# Initializing the model
m = Model()


