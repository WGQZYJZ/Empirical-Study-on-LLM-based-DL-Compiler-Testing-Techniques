
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x = torch.nn.functional.conv2d(x, ...) # The conv2d function has multiple input dimensions
        x = torch.nn.functional.batch_norm(...)  # Follow the same pattern for batch norm.

        return output

# Initializing the model
m = Model()

