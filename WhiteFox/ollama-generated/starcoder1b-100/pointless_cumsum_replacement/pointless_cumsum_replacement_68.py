
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        v = torch.full((x.shape), 1, dtype=x.dtype, layout=x.layout, device=x.device, pin_memory=False)
        for i in range(20):
            v += x
        return v


# Inputs to the model
inputs = torch.randn(5, 3, 64, 64)
