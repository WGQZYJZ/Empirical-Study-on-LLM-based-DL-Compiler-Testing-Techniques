
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
    
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 * 0.5 + other_tensor
        v3 = torch.relu(v2) # Replace ReLU with a LeakyReLU
        return v3

# Initializing the model
m  = Model()


# Inputs to the model
other_tensor = torch.randn(4, 8, 64, 64).cuda().float()
x1 = torch.randn(4, 3, 64, 64) # different from the previous input tensor x

# Model output
__output__  = m(x1)

