
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if other is None:
            self.other = torch.zeros(1, 3, 64, 64) # Constant value zero tensor, same shape as the input tensor
        else:
            self.other = other
 
    def forward(self, x):
        v1 = self.conv(x) + self.other
        return v1

# Initializing the model with the following two input tensors
m = Model(input_tensor_2) # Add another constant value tensor to each output of a convolution
