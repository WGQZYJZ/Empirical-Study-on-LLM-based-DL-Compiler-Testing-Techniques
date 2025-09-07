
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

 # Set a constant to subtract from the output of the convolution
other = torch.zeros(8, dtype=torch.float32).to("cpu")

 # Calculate and print the output tensor
