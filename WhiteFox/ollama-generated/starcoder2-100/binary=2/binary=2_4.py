
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor) -> None:
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = other
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - self.other
        return v2


# Initializing the model and setting its input tensor for inference (if applicable). You can set this to None when no such setting is available. 
m      = Model(None if not hasattr(m, 'other') else m.other)

