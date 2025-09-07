
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.dense = torch.nn.Linear(1046, 256)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5 + torch.randn(x1.shape[0], v1.shape[1]//2) # Randomly initialize a new tensor with shape (x1.shape[0], v1.shape[1]//2) using the normal distribution and add it to the output of the convolution
        v3 = self.dense(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5, 3, 64, 64)
