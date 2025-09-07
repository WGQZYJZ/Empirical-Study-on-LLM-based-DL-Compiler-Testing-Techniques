
class Model(torch.nn.Module):
    def __init__(self, size=9223372036854775807):
        super().__init__()
        self.conv = torch.nn.Conv1d(size + 1, 10, 1)

    def forward(self, *args):
        x = torch.cat([torch.cat(args, dim=1), args[2][:, :, 0:9223372036854775807]],
                      dim=1)
        y = self.conv(x)
        return y


# Initializing the model
m  = Model()
