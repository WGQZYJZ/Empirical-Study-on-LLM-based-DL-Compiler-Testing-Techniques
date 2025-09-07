

class MyModel(torch.nn.Module):
    def __init__(self, conv=50, batchNorm=False):
        super().__init__()
        
        self.conv  = torch.nn.Conv2d(1, 32, kernel_size=(4, 4), stride=1, padding="SAME", bias=True)
        if batchNorm == True:
            self.bn   = torch.nn.BatchNorm2d(num_features=32)

        self._output = [self]

    def forward(self, *args):
        result  = self.conv(*args).relu()

        if hasattr(self, 'bn'):
            result  = self.bn(result)

        return result


# Initializing the model
model   = MyModel()

# Inputs to the model
input1     = torch.randn(32*8*4096)
__output__  = model(input1)

