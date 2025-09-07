
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
 
    def forward(self, x):
        v = self.conv1(x)
        v = torch.tanh(v)  # ReLU activation function for the first hidden layer
        v = self.conv2(v)
        v = torch.sigmoid(v)
        return v


# Initializing the model
m = Model()

