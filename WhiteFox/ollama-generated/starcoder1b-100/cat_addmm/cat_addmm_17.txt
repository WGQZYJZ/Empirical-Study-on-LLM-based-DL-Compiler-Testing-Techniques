
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3)
        self.conv2 = torch.nn.Conv2d(8, 16, 4)
        self.fc    = torch.nn.Linear(16 * 5 * 5, 10)
 
    def forward(self, x):
        v1 = F.relu(self.conv1(x))  # Convolutional Layer 1
        v2 = F.max_pool2d(v1, 2, stride=2)  # Pooling Layer 1 with a window size of (2, 2) and a step of (2, 2).
        v3 = F.relu(self.conv2(v2))   # Convolutional Layer 2
        v4 = F.max_pool2d(v3, 2, stride=2)  # Pooling Layer 2 with a window size of (2, 2) and a step of (2, 2).
        v5 = torch.flatten(v4, start_dim=-1)   # Flatten the 4D input to a 2D one, so that 20x4 is now 20. This operation can be done in two ways:
        20*5*5 + 16
        v5 = torch.cat([v5], dim=1)     # Concatenate the 4D output to the end of the input tensor, so that the resulting shape is (20, 320).
        
        v6 = F.relu(self.fc(v5))       # Fully Connected Layer 1
        return v6


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
