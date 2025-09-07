
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1[:, :, :96])
        v2 = torch.cat([v1[:, :, :96], x1[:, :, 96:]], dim=-1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
input_tensors = [
    x1,
    x1 * 0.5,
    torch.erf(torch.cat([x1, x1], dim=1)),
    0.7071067811865476
]


# __output__ should be equal to input_tensors