
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1  = torch.nn.Conv2d(...)

    def forward(self, x):
       v1  = torch.nn.functional.conv1d(..., self.conv1)
       return torch.nn.functional.batch_norm1d(..., self.conv1, self.conv1)

m  = Model()

x  = torch.randn(1, 3, 500)
__output__  = m(x)

