
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 5 # Adding a constant to the output of convolution
        v4 = torch.relu(v2) # Applying ReLU function on the result after addition
        return v3


# Initializing the model and passing the input tensor