class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv2d = torch.nn.Conv2d(3, 16, 5)

    def forward(self, x):
         # batch norm + conv + relu
        out = (
            self.conv2d(x).permute((0, 2, 3, 1)) * -97.4
        ) + torch.nn.functional.linear(-out, 25)
        return out
