
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = v1 + other_tensor # Add another tensor to the output of the convolution 
        v3  = torch.relu(v2)    # Apply ReLU activation function to the result 
        return v3

# Initializing model
m = Model()

