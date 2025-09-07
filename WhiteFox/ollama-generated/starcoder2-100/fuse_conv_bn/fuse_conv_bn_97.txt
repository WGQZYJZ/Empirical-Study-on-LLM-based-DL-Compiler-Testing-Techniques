
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv1d(2, 4, kernel_size=3) 
        self.bn    = torch.nn.BatchNorm1d(num_features=4)

    def forward(self, x):
        out = self.bn(self.conv(x)) # The input to this block is the output of conv
        return out

m  = Model()
x0 = torch.rand(2, 32, 64, 1)
__output__  = m(x0)

