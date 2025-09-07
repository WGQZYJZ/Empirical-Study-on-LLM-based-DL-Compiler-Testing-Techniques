
class Model(torch.nn.Module):
    def __init__(self, num_conv1x1s=2):
        super().__init__()
        self.conv  = torch.nn.Conv3d(4096, 512, kernel_size=(1, 7, 7), stride=(1, 2, 2), padding=(0, 3, 3))
        self.norm  = torch.nn.BatchNorm3d(num_features=512)

    def forward(self, x):
      for i in range(self.__class__.conv1x1s):
            x = self.norm(self.conv(x))
            return x

m = Model()

