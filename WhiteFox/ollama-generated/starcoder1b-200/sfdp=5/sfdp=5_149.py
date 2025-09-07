
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.mean(v1, dim=(1,2))
        v3 = self.conv(x2)
        v4 = torch.mean(v3, dim=(1,2))
        qk  = v2 @ v3 / (torch.sqrt(torch.mm(v2, v3)))
        attn_weight = torch.softmax(qk, dim=-1)
        return attn_weight @ v4


# Initializing the model
m = Model()
