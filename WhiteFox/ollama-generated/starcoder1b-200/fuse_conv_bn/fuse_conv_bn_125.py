
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.functional.conv2d(...) # X should be 3 representing the number of channels
        bn  = torch.nn.functional.batch_norm(...) # X should be the same as the output of the conv layer

        v1 = bn(conv(x1))
        return v1


# Inputs to the model
x1 = torch.randn(2, 3, 50, 50)
