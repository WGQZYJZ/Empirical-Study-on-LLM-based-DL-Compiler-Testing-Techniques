
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 2, kernel_size=2)

    def forward(self, x1):
        v1 = self.conv(x1) # Bias not considered for BatchNorm
        v2 = v1 * v1 
        v2 = torch.nn.functional.batch_norm(v2, v2, affine=False, training=True)
        return v2


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 4, 4) # Bias not considered for BatchNorm
