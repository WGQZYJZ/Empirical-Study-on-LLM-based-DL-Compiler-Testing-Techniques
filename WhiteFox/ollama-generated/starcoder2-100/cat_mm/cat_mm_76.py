class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.fcn = torch.nn.Linear(64*96, 50)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply pointwise convolution with kernel size 3 to the input tensor of shape [batch_size x 8 x 27 x 27]
        v2 = torch.nn.functional.max_pool2d(v1, kernel_size=4, stride=(4, 6), padding=0) # Apply max pooling with kernel size 3 to the input tensor of shape [batch_size x 8 x 9 x 7]
        v3 = self.fcn(torch.flatten(v2)) # Flatten and apply pointwise linear transformation on the output of maxpooling operation
        return v3
