
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.conv = torch.nn.Conv2d(3, 8, 5)

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.nn.functional.batch_norm(v1, running_mean=None, running_var=None, momentum=0.9, eps=0.001)

        return v2

m = Model()

