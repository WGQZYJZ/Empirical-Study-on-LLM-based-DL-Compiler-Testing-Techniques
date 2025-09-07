
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear  = torch.nn.Linear(64 * 64, 8)
 
    def forward(self, x):
        # t1 = m.conv(x) # Apply a pointwise convolution to the input tensor
        t2 = F.relu(self.conv(x))  # Apply the ReLU activation function to the output of the convolution
        return self.linear(t2)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
