
class Model(torch.nn.Module):
    def __init__(self, input_dim, output_dim=10):
        super().__init__()
        self.conv = torch.nn.Conv2d(input_dim, 32, 1, stride=1, padding=1)
        self.pooling = torch.nn.MaxPool2d((2,2), stride=(2,2))
        self.fc = torch.nn.Linear(4*4*32, output_dim)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.pooling(v1)
        v3 = v2.view(-1, 4 * 4 * 32)
        v4 = self.fc(v3)
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(8000, 32, 64, 64)
