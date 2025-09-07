
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.nn.functional.conv2d(x1, weight=2) + 3 * \
            (torch.nn.functional.batch_norm2d(
                conv1, training=True, track_running_stats=False))


# Initializing the model