
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(16, 16, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv1(x1)  # Apply convolution on the input to obtain the hidden state (t1)
        v2 = torch.tanh(v1)  # Apply the Tanh activation function on the output of the previous layer t1
        v3 = self.conv2(v2)  # Apply a second convolution on the hidden state and obtain its representation (t2)
        v4 = torch.relu(v3)  # Apply the Relu activation function on the output of the third layer t2
        v5 = self.conv3(v4)  # Apply a third convolution on the hidden state and obtain its representation (t3)
        return v5

# Initializing the model
m = Model()


