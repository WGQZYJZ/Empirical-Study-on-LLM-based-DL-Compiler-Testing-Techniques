
class Model(torch.nn.Module):
    def __init__(self, hidden_size=128):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 4, 5, stride=2)
        self.conv2 = torch.nn.Conv2d(4, 8, 5, stride=2)
        self.fc = torch.nn.Linear(hidden_size * 28 * 28, hidden_size)
 
    def forward(self, x1):
        # (b, c, h_in, w_in) -> (b, c, 4, 4) -> (b, 4, 8, 8) -> (b, 4, 28, 28)
        v = self.conv1(x1).view(x1.shape[0], -1)  # Reshape the input to 1-D (Numpy array of size N x H) for broadcasting
        # (b, h_in*w_in, c) -> (b, h_in*w_in, 4) -> (b, 4, 8) -> (b, 4, 28) -> (b, 128)
        v = self.conv2(v).view(-1, 5 * 5 * 8)  # Reshape the input to 2D (Numpy array of size N x C x H*W), then convert it to a batch of 4-D matrices for broadcasting
        v = v.view(x1.shape[0], -1, self.fc.in_features)  # View to 3D (b * N * C) to match the model. The size of `x1` must not change, as a view is performed on the fly during a backward pass
        v = self.fc(v)  # Apply linear transformation using the output of the previous layer as input for the current layer
        return v


# Initializing the model
m = Model()


