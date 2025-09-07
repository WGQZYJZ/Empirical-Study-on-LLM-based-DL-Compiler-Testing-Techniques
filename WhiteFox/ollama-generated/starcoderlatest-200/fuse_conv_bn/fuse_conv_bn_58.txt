
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(...)

    def forward(self, x):
        output = self.conv(x) # BatchNormalization(activation=True)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 2, 5)
