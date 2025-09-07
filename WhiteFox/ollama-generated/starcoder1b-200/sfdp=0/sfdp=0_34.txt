
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(8)
        self.linear1 = torch.nn.Linear(8 * 5 * 5, 8 * 7 * 7)
        self.dropout = torch.nn.Dropout(0.4)
        self.conv2 = torch.nn.Conv2d(8 * 7 * 7, 3, 1, stride=1, padding=1)
        self.linear2 = torch.nn.Linear(8 * 7 * 7, 8)
 
    def forward(self, x):
        # (batch_size, channels, height, width)
        b  = x.shape[0]
        x  = F.leaky_relu(self.bn1(self.conv1(x)))
        x  = x.view(-1, 8 * 7 * 7)
        x  = self.linear1(x)
        x  = self.dropout(F.relu(self.linear2(x)))
        x  = self.conv2(x)
        return F.softmax(x, dim=1)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(3, 8, 56, 56)
