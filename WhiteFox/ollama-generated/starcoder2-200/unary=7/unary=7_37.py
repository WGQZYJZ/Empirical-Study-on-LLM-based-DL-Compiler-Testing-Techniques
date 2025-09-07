
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(8, 64, 7, 4, 1)
 
    def forward(self, x):
        l1 = self.conv1(x) # Apply the first convolution to the input tensor
        l3 = self.conv2(l1 + 4)# Apply the second convnet to the output of the first convolution added with `4`
# Inputs for the model
i  = torch.randn(8, 3, 500, 500) # Input tensors should be 8 x 3 x 500 x 500
