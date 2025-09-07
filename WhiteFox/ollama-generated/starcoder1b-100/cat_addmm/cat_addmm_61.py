
class Model(torch.nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.fc1 = torch.nn.Linear(4096, 256) # The input data should be of shape (batch size, number of pixels/feature map width * height * channels)
        self.fc2 = torch.nn.Linear(256, 128)
        self.fc3 = torch.nn.Linear(128, num_classes)
 
    def forward(self, x): # Forward pass
        v1 = x.view(-1, 4096) # Flatten the input data to a single vector
        v2 = self.fc1(v1) # The result of a matrix multiplication is of shape (batch size, 256), so multiply it by the value 0.5 and concatenate the result along dimension 1.
        v3 = self.fc2(v2)
        v4 = torch.tanh(v3) * 0.7 # Apply tanh nonlinearity to the results of a matrix multiplication and multiply it by 0.7 (or other constant).
        v5 = self.fc3(v4)
        return v5


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64) # Batch size must be specified and equal to 2
