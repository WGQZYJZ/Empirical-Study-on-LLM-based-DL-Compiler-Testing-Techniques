
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        t1 = torch.cat([v1, v1], dim=-1)
        v2 = torch.cat(
            [
                v1[:, :, :-3, :-3] * 0.5 + v1[:, :, 3:, 3:],
                v1[:, :, 1:-1, :] * 0.7071067811865476,
            ],
            dim=-1,
        )
        t2 = torch.cat([v2, v2], dim=-1)
        t3 = torch.cat(
            [
                v1[:, :, :-3, 3:] * 0.5 + v1[:, :, 3:, :-3] * 0.7071067811865476,
                v1[:, :, 1:-1, :] * 0.7071067811865476,
            ],
            dim=-1,
        )
        t4 = torch.cat([t3, t3], dim=1)
        return t4


# Initializing the model
m = Model()


