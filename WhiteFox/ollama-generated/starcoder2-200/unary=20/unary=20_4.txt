
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(8 * 3, 3, kernel_size=3)
        self.conv2 = torch.nn.Conv2d(8 * 5, 3, kernel_size=3)
        self.conv3 = torch.nn.ConvTranspose2d(8, 16, 4)
    
    def forward(self, x):
       x1  = self.conv1(x) 
       x2  = self.conv2(torch.relu(x1))   # Apply ReLU to the output of transposed convolution
       x3  = torch.sigmoid(x2)             # Apply sigmoid to the output of transposed convolution
       x4  = self.conv3(x3, output_size=(160 + 8 * 5 - (3 - 1), 97))
       return x4
 
# Initializing the model
m = Model()


# Inputs to the model