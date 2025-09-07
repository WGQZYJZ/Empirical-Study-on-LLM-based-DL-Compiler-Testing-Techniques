
class Model(torch.nn.Module):
    def __init__(self, conv1d=2, conv3d=2):
        super().__init__()

        self.conv1d = torch.nn.Conv1d(conv1d, 2, kernel_size=(3,), padding=(0,))
        self.conv3d = torch.nn.Conv3d(
            conv3d, 4, kernel_size=((2), (3)), padding=(0,)
        )

        self.bn = torch.nn.BatchNorm3d(self.conv1d)

    def forward(self, input):

        v1 = self.bn(self.conv3d(input))
        
        return v1

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(20, 5, 7)

__output__  = m(x1)


