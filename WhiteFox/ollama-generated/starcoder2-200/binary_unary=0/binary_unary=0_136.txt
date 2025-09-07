
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 + torch.randn_like(v1).type_as(v1) # Add another tensor to the output of the convolution 
        v3  = torch.relu(v2)  # Apply ReLU activation function to the result 
        return v3

# Initializing model
m = Model()

