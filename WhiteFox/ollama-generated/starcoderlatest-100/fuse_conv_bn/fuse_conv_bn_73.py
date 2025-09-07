
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(...)
        self.bn = torch.nn.BatchNorm1d(...)

    def forward(self, x1):
        output = self.conv(x1)
        output = F.batch_norm(output)
        return output

# Inputs to the model
x1 = torch.randn(1, 2, 2)
