
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(2, 4, kernel_size=5)
        self.bn = torch.nn.BatchNorm1d(num_features=4)

    def forward(self, x):
        # TODO: Implement the pattern of conv -> bn
        return None


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 2, 3)
