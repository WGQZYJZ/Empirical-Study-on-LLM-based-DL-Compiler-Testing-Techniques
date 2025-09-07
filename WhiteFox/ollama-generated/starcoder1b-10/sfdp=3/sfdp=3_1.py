
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc = torch.nn.Linear(8, 50)

    def forward(self, x):
        # Do the first convolutional layer
        x = self.conv1(x)
        # Apply a linear operation to get an embedding representation of size (batch_size, input_seq_len, hidden_dim)
        x = torch.relu(self.fc(x))
        return x

# Initializing the model
m = Model()

