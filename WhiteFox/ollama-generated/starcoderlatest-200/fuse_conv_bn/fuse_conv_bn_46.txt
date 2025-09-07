
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        conv = torch.nn.functional.conv2d(x)
        bn   = torch.nn.functional.batch_norm(conv)
        return bn


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 14, 14)
