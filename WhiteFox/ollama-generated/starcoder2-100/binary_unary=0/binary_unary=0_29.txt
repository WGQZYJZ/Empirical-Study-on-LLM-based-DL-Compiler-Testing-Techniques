
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other): # other is a new input tensor with the same shape as x1
        v1 = self.conv(x1) 
        v2 = v1 + other  # Adding another tensor to the output of the convolution operation
        v3 = torch.relu(v2)   # Applying ReLU activation function
        return v3

# Initializing the model