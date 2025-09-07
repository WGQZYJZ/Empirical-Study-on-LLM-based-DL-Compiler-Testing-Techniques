 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 16, kernel_size=5)
        self.bn1 = torch.nn.BatchNorm2d(16)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        conv1_out = self.conv1(x)
        bn1_out   = self.bn1(conv1_out)
        relu_out  = self.relu(bn1_out)

# Initializing the model
m = Model()


