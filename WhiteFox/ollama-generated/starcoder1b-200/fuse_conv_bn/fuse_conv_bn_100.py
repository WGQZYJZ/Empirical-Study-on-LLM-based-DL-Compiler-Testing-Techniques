
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(...) # X can be 1, 2 or 3 representing the dimension
        self.bn    = torch.nn.BatchNorm2d(...) # X should match with Conv2d

    @torch.jit.script_method
    def forward(self, x):
        output = self.bn(self.conv(x))
        return output


# Initializing the model
m = Model()

