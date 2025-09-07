
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor = None) -> None:
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if other is not None:
            self.other = other

    def forward(self, x):
        v1  = self.conv(x)
        if self.other is not None: # This part makes sure the output tensor is non-zero
            v2  = torch.zeros_like(v1)
        else:
            v2  = self.other + v1 # The second convolution and subsequent steps are omitted for simplicity of explanation
        return v2

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
