
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 + self.other # Add a second tensor to the output of the convolution
        v3 = torch.relu(v2)  # Apply the ReLU activation function to the result
        return v3

# Initializing the model with randomly generated input tensors
m = Model()
 
x1 = torch.randn(1, 3, 64, 64) 

# Adding a second randomly generated tensor
m.other = torch.randn(1, 8, 64, 64) * .5 + .707 # add the second tensor

 # Run inference on the model with the initial and modified input tensors to generate output
__output_before__  = m(x1)
m(x1)
 
__output_after__  = m(x1)
