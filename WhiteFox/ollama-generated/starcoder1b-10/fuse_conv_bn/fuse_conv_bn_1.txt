
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2=None):
        self.conv = torch.nn.functional.conv2d(...)  # X can be 1, 2, or 3 representing the dimension
        self.batch_norm = torch.nn.BatchNormXd(...)  # X should match with ConvXd

        if x2 is not None:
            self.conv2 = ...
            self.batch_norm2 = ...
        return output


# Initializing the model
m = Model()


