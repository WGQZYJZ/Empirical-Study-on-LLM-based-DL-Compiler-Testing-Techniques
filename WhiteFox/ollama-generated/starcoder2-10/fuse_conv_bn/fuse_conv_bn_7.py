
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.conv1 = torch.nn.Conv2d(3, 40, kernel_size=(5, 5))

        self.conv2 = torch.nn.Conv2d(80, 60, kernel_size=(5, 5), padding=1)

        self.bn1 = torch.nn.BatchNorm2d(20, track_running_stats=True)
        self.bn2 = torch.nn.BatchNorm2d(40)

        # initialize weight and bias using Xavier initialization
        for m in [self.conv1]:
            n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
            for param in m.parameters():
                if hasattr(m, 'bias') and m.bias is not None:
                    nn.init.constant_(param, 0) # initializing bias as zero
                elif isinstance(m, torch.nn.Conv2d):
                    nn.init.xavier_normal_(param.data)
                else:
                    raise Exception('unsupoorted weight initialization')
    def forward(self, x1):
        v1 = self.bn1(torch.nn.functional.conv2d(
            x1, self.conv1.weight))

        v2 = torch.nn.functional.batch_norm(v1, self.bn2.running_mean)
        return v2

# Initializing the model
m  = Model()
