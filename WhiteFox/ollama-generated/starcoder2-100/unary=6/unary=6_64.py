class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1): 
        v1 = self.conv(x1) # Apply a pointwise convolution to the input tensor

        # Pass the output through one or more ReLU activation functions (in this case only one)
        v2a = torch.nn.functional.relu(v1 * 0.5) 
        v3b = torch.nn.functional.relu(v2a + 3) 
        v4c = torch.nn.functional.relu(v3b / 6)
        return v4c
