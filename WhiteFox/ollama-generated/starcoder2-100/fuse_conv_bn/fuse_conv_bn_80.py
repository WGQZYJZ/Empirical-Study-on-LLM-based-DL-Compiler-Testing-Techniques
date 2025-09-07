
class Model(torch.nn.Module):
    def __init__(self, channel=4096, num_classes=1000):
        super().__init__()
        self.base  = torch.nn.Conv2d(3, channel, kernel_size=(7, 7), padding=(3, 3))

        self.head = torch.nn.Sequential(
            torch.nn.Linear(channel * 1440 + num_classes, 512)
        )

    def forward(self, input):
        base  = self.base(input) # conv1
        batchnorm  = torch.nn.BatchNormNd(base) # bn1
        output  = torch.nn.functional.linear(batchnorm, self.head)
        return output

model = Model()
output  = model(torch.randn(4, 3, 299, 299))

