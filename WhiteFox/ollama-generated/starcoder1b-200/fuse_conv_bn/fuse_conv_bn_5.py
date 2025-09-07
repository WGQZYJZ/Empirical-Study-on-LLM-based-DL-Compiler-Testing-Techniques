
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        output = torch.conv2d(...)  # X can be 3 or 4 representing the number of input channels
        output = batch_norm(output)  # The module API equivalent of this is `batch_norm(...).apply(...)`

        return output


# Initializing the model
m = Model()

