
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other # Add another tensor to the output of the convolution
        v3 = torch.relu(v2) 
        return v3

# Initializing the model
m  = Model()


# Inputs to the model
x1, other = torch.randn(1, 3, 64, 64), torch.randn(1, 8, 32, 32) # Generate two random tensors that you want to add together 

# __output__  = m(x1)

# Submit Answer: