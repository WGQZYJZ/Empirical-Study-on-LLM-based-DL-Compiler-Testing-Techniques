
class Model(torch.nn.Module):
    def __init__(self, d_model=512):
        super().__init__()
        self.scale = torch.sqrt(torch.FloatTensor([d_model]))
        self.W1 = torch.nn.Linear(3, d_model)  # Apply linear transformation to the input of a convolutional layer
        self.conv = torch.nn.Conv2d(d_model, 8, 1, stride=1, padding=1)  # Apply pointwise convolution with kernel size 1
        self.W2 = torch.nn.Linear(d_model, d_model)  # Apply linear transformation to the output of a convolutional layer
 
    def forward(self, x1):
        v1 = F.relu(self.W1(x1))  # Apply rectified Linear transformation to the input tensor
        v2 = self.conv(v1) * self.scale  # Scale the input of the convolutional layer
        v3 = torch.erf(self.W2(v2).mul(0.7071067811865475))  # Apply the error function to the output of the convolution layer
        return v3


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
