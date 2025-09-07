
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other # Replace the "other" in the example with another tensor or scalar to make the model different from the previous one
        v3 = torch.nn.ReLU()(v2)
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
 
# Output of the model without replacement for "other" in the pattern (to reproduce the original example)
