
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + 3
        v2 = torch.clamp_min(v1, 0)
        v3 = torch.clamp_max(v2, 6)
        v4 = v3 / 6
        return v4


# Input to the model: [tensor([[[-1.5596,  1.2782]],

        [[-0.0254, -0.2398]],

        [[-0.2101, -0.6940]]]), grad_fn=<MulBackward0>], requires grad=True)]
t1 = torch.clamp_min(v4, 0)
