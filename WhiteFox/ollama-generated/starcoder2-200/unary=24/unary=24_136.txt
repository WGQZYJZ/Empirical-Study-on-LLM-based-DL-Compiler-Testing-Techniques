
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 > 0
        v3  = v1 * negative_slope # Negative slope is the negative of the positive slope in Leaky ReLU activation function. 
        v4  = torch.where(v2, v1, v3) # If mask == True, set output equal to value; else output will be negative value
        return v4


# Initializing the model with a specific negative_slope of 0.1 (The default negative slope is 0.1.)
m = Model(negative_slope=0.1)
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
 
 # Predict the output using the input tensor x1 for the model m and print its size in the shape of (8, 25, 64, 64).
 
