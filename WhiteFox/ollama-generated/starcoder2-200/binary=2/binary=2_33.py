
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        return v2


# Initializing the model with a different tensor for the input.
m = Model(torch.randn([3, 8, 64, 64])) # The tensor is randomly generated using torch.randn.

# Inputs to the model (the tensor will be different from that used in Model).
x1 = torch.randn(2, 3, 64, 64)

