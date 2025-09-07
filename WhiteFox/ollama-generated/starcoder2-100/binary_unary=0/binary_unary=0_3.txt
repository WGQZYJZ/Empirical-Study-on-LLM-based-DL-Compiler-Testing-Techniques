
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
         v1  = self.conv(x1) + other # other is a different tensor from the one used in __output__
         v2  = torch.relu(v1)
         return v2

# Initializing the model
m  = Model()


# Inputs to the model
other = torch.randn(1,8,64,64).requires_grad_(True) # A tensor with requires_grad=True will be used as an input for adding to a convolutional output in order to ensure that this pattern is not broken. 
x1   = torch.randn(1,3,64,64)

