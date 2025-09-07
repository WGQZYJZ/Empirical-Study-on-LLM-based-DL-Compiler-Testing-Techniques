
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc = torch.nn.Linear(8, 40)
 
    def forward(self, x1):
        # First convolutional layer
        v1 = self.conv1(x1)  # Compute the dot product of the query and a key
        v2 = torch.tanh(v1)  # Compute the dot product of the output of the first convolutional layer with the tanh activation function
        # Then FC layer to obtain predictions
        v3 = self.fc(v2)
        return v3


# Initializing the model
m = Model()

