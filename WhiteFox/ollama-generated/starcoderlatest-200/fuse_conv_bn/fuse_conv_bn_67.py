
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.conv2d(x1, ..., stride=...)
        v2 = torch.nn.functional.batch_norm(...) # bn_input is v1

        return v2


# Inputs to the model
x1 = torch.randn(1, 4, 4)
