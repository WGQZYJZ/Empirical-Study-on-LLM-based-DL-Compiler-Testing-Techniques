
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 7, stride=2, padding=3) # kernel size of (7,7), stride of (2,2) and padding of (3,3) 
        self.conv2 = torch.nn.Conv2d(64, 128, 5, stride=2, padding=3) # kernel size of (5,5), stride of (2,2) and padding of (3,3) 
        self.flatten = torch.nn.Flatten()

    def forward(self, x1):
        v1 = F.relu(self.conv1(x1))  # Apply ReLU activation function on the output of convolution layer 1 with input as x1
        v2 = F.relu(self.conv2(v1))  # Apply ReLU activation function on the output of convolution layer 2 with input as v1, note that this is in parallel
        v3 = self.flatten(v2)    # Flatten the output of convolution layer 2 
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
