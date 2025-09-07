

class Model(torch.nn.Module):
    def __init__(self, n_classes=10):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        v1 = F.relu6(self.conv(x1))
        return v1

# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn((20,3, 547, 985))

# Input for the conv layer of the model is random. Hence, it is not provided as a part of initial model input.

output = m(input)
