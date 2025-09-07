
class Model(torch.nn.Module):
    def __init__(self, size1=32):
        super().__init__()
        self.conv  = torch.nn.Conv2d(in_channels=size1, out_channels=8, kernel_size=(7), stride=(1), padding=(0))
        self.pool = torch.nn.AvgPool2d((4, 5))
        self.relu = torch.nn.ReLU()

    def forward(self):
         return self.relu(
            self.conv(
                self.pool(
                    self.conv3(
                        self.conv2(
                            self.conv1(
                                torch.rand([8, 3, 4, 5])
                             )
                         )
                     )
                 )
             )
        )

model = Model()


