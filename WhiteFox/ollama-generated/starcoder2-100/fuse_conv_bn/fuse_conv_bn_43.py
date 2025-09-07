
class FusedModel(torch.nn.Module):
    def __init__(self, conv, bn):
        super().__init__()
        self.conv = conv

    def forward(self, x1):
        x2  = torch.nn.functional.conv3d(x1, self.conv)
        return torch.nn.functional.batch_norm3d(x2)

# Initializing the model
m = FusedModel(...)

