
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        # x: [B, C, H, W]
        # h: [B, C // 4, H // 4, W // 4]
        h = self.conv1(x)
        h = h.view(-1, 8, int(h.size()[2] / 4), int(h.size()[3] / 4))
        # h: [B, 8, H // 4, W // 4]
        h = self.conv2(h)
        h = h * (0.25 + 1)
        # h: [B, C // 4, H // 4, W // 4]
        return h


# Initializing the model
m = Model()


