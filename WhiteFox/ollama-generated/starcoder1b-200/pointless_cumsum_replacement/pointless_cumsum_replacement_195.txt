
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        return (v1 * 0.5).cumsum(1), (v2 * 0.7071067811865476).cumsum(1)


# Initializing the model
m = Model()


