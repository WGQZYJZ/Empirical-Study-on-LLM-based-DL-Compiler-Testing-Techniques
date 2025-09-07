
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # The input is an 8-channel tensor of shape [B, 320]
        v1 = torch.nn.functional.interpolate(x1[None], size=(64,), mode='nearest')
        v2 = torch.clamp_min(v1[:, :, None, None].expand(-1, -1, 8, 8), min=0)
        v3 = torch.clamp_max(v2, max=-59.75132751464844)

        return v3


# Initializing the model
m = Model()
x1 = torch.randn(2, 8, 320)

__output__  = m(x1)