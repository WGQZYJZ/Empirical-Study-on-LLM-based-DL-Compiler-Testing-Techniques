
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.nn.functional.conv2d(...)  # X can be 3, 4, or 5 representing the number of input channels
        return torch.nn.functional.batch_norm(...)  # X should match with ConvNd


# Initializing the model
m = Model()


