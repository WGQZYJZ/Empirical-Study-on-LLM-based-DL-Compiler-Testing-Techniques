
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(...)

    def forward(self, x1):
        conv_output = self.conv1(x1)
        bn_output = F.batch_norm(conv_output, ...)
        return bn_output
