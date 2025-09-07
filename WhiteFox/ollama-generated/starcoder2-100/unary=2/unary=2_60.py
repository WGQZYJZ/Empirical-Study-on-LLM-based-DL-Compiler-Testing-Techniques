
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.deconv(x1) # Apply pointwise transposed convolution to the input tensor
        v2 = v1 * 0.5        # Multiply the output of the transposed convolution by 0.5
        v3 = torch.nn.functional.relu(v2 + v2 + v2, inplace=True)# Add the output of the transposed convolution and the result of multiplication to 3 times the output of the addition, and then apply the ReLU function to this result
        v4 = torch.nn.functional.relu(v1 * t3, inplace=True) # Multiply the output of the transposed convolution by another constant, add it with the output of the multiplication, and then apply the ReLU function to this result
        v5 = v2 + 0.7978845608028654  # Add 0.7978845608028654 to the output of the transposed convolution
        v6 = torch.nn.functional.relu(v3 * t1, inplace=True)    # Multiply the result of addition by another constant, and then apply the ReLU function to this result
        v7 = 1 + v1   # Add 1 to the output of the transposed convolution 
        v8 = torch.nn.functional.relu(v4 * t2, inplace=True)     # Multiply the result of multiplication by another constant, and then apply the ReLU function to this result
        return v5  # Return the output of the addition


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64) 

