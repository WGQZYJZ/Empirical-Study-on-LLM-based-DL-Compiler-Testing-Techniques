 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)

    def forward(self, x1):
        bn = torch.nn.functional.batch_norm(..., ...)
        return bn(self.conv(x1))


# Initializing the model
m = Model()
# Input tensor to the model
x1 = torch.randn(2, 3, 4, 5)
