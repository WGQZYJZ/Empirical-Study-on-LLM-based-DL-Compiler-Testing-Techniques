
class Model(torch.nn.Module):
    def __init__(self, n_features=128):
        super().__init__()
        self.fc1 = torch.nn.Linear(3 * 64 * 64, 5 * 16)
        self.fc2 = torch.nn.Linear(n_features, 7)

    def forward(self, x1):
        # Flatten a tensor of shape [batch, channel, height, width] to a vector of shape [batch * channel * height * width]
        x1 = x1.view(x1.size(0), -1)

        # Apply two linear transformations on the input
        x2 = self.fc1(x1).view(x1.size(0), -1)
        x3 = self.fc2(x2).view(x1.size(0), -1)

        # Return the output of this linear transformation as an output tensor
        return x3


# Initializing the model
m = Model()
__output__  = m(input_tensor)

