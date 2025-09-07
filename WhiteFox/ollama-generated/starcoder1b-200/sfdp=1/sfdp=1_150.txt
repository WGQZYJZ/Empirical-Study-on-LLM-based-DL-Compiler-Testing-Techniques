
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc    = torch.nn.Linear(512, 64)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(self.fc(v1))  # Apply the sigmoid function to the output of a pointwise convolution
        v3 = torch.exp(v2) - 1  # Calculate the logit function of the output of the sigmoid function
        v4 = v3 * (x1 - x2)  # Calculate the output of the softmax function by the dot product of the value tensor and the output of a pointwise convolution
        v5 = torch.softmax(v4, dim=-1)  # Apply softmax to the output of the softmax function
        return v5


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
