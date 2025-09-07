
class Model(torch.nn.Module):
    def __init__(self, n_classes=10):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, kernel_size=(1, 1)) # Apply convolution with kernel size (1, 1) to the input tensor
        self.fc1 = nn.Linear(8*64*64, n_classes, bias=True)
 
    def forward(self, x):
        v1 = self.conv(x) # Apply convolution
        v2 = torch.flatten(v1, start_dim=1) # Flatten the output of the convolution
        v3 = self.fc1(v2) # apply fully connected with n_classes neurons and bias to v2
        return v3


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
