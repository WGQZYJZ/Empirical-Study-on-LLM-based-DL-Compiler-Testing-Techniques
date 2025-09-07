
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.conv  = torch.nn.Conv2d(dim, dim // 2, 1, stride=1, padding=0)
        self.pool  = torch.nn.MaxPool2d((2, 2), ceil_mode=True)
        self.dense = torch.nn.Linear(dim // 2, dim)
 
    def forward(self, x):
        x1 = self.conv(x)
        x2 = self.pool(x1)
        x3 = self.dense(x2)
        return x3


# Initializing the model
m  = Model(8)


# Inputs to the model
x1  = torch.randn(5, 64, 64)
