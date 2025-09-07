
class Model(torch.nn.Module):
    def __init__(self, num_layers=3):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1)

        for i in range(num_layers-2):
            self.conv2 = torch.nn.Conv2d(8, 8, 1)
    def forward(self, x):
        v1  = self.conv (x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 - other    # Subtract 'other' from the output of the convolution
        return v2


# Initializing the model
m  = Model(num_layers=5).cuda() # This model contains 4 pointwise convolutions with kernel size 1, and one additional pointwise convolution layer. The number of layers could be any integer greater than or equal to two.
x1 = torch.randn(2, 3, 64, 64)


# Evaluating the model without 'other'
m.eval()
