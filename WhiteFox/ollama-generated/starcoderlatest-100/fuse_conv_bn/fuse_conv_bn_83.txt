 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(...)
        self.bn = torch.nn.BatchNorm1d(...)

    def forward(self, x1):
        output = self.bn(self.conv(x1))
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2048, 3) # batch size 1 and sequence length 2048
