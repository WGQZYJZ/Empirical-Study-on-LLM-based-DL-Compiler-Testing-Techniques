
class Model(torch.nn.Module):
    def __init__(self, hidden_size=256, batch_norm_momentum=0.1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1) + x2
        return self._apply_batch_norm(v1)
 
    @staticmethod
    def _apply_batch_norm(x1):
        # Batch normalization with momentum 0.1.
        return torch.nn.BatchNorm2d(momentum=0.1)(x1)


# Initializing the model
m = Model()
x1, x2 = torch.randn(1, 3, 64, 64), torch.randn(1, 8, 64, 64)
