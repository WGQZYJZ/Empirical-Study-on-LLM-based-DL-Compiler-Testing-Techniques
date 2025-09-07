
class Model(torch.nn.Module):
    def __init__(self, num_classes=1000):
        super().__init__()
        self.fc1 = torch.nn.Linear(64 * 64, 256)
        self.fc2 = torch.nn.Linear(256, num_classes)
 
    def forward(self, x):
        # Reshape the input to [batchsize x channels x width x height] and perform a matrix multiplication with an affine transformation (affine layers).
        out = self.fc1(x.view(-1, 64 * 64)).view(x.shape[0], -1)
        # Perform the affine transformation, i.e., add b to each feature vector in each sample [batchsize x features].
        out = out + torch.randn(out.shape) * 20
        # Apply a sigmoid function (and clip it to prevent saturation and overflow), then convert the outputs into a matrix where each sample has one column and each value between -1 and 1 is mapped to an index in `num_classes`.
        out = torch.sigmoid(self.fc2(out))
        return out


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 64, 64)
