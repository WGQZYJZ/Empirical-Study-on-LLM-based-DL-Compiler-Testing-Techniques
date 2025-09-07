
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1) # Conv Layer (kernel size 1; stride 1; padding 1)
        self.conv2 = torch.nn.Conv2d(3, 32, 4, stride=2, padding=1) # Conv Layer (kernel size 4; stride 2; padding 0)
        self.fc1 = torch.nn.Linear(48*4*4, 128) # Linear Transformation Layer (input dim: 48*4*4; output dim: 128)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.nn.functional.flatten(v2, start_dim=1) # Flatten the output of the second convolution layer to a 1D tensor
        v4 = self.fc1(v3) # Apply linear transformation layer with input dim 48*4*4 and output dim 128
        v5 = torch.nn.functional.relu(v4) # Apply ReLU activation function on the output of linear transformation layer
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
