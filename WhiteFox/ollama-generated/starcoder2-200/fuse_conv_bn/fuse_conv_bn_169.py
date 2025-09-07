
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1  = torch.nn.Conv2d(3, 480, kernel_size=(5, 7), stride=(2, 1))
        self.norm1  = torch.nn.BatchNormNd(480)

    def forward(self, x):
         x1   = x
         x    = torch.nn.functional.batch_norm(x1, None, None, self.norm1.weight, self.norm1.bias, False, self.norm1.eps)
         x  = self.conv1(x) + x
        return x

# Initializing the model
m  = Model()

# Inputs to the model
x   = torch.randn(2560, 32, 896, 47)

