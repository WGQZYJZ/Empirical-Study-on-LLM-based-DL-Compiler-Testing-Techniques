
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=5) # Apply pointwise convolution to the input tensor with the size of the kernel as 5.
        self.linear = torch.nn.Linear(4096, 7)
        self.drop1 = torch.nn.Dropout()
        self.drop2 = torch.nn.Dropout()
    
    def forward(self, x):
        v_conv1 = self.conv1(x)
        v_flat = flatten(v_conv1, start_dim=0) # Flatten the output of the pointwise convolution to 1-dimensional array
        v_linear = self.linear(v_flat)
        v_drop1 = self.drop1(v_linear) # Apply dropout with probability of 0.5
        v_drop2 = self.drop2(v_drop1)
        
        return v_drop2


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(3, 3, 4968, 70) # Input with shape of [3 (batch size), 3 (channel number), 12*12 (height/width), 7]
