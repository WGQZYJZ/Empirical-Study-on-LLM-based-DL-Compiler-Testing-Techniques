
class Model(torch.nn.Module):
    def __init__(self, dropout_p=0.1, dropout_q=0.2):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(8)
        self.layer1 = torch.nn.ReLU()
        self.conv2 = torch.nn.Conv2d(8, 8, 2, stride=2, padding=0)
        self.bn2 = torch.nn.BatchNorm2d(8)
        self.layer2 = torch.nn.ReLU()
        self.pool = torch.nn.AdaptiveAvgPool2d((1, 2))
        self.dropout = torch.nn.Dropout2d(p=dropout_p)
        self.linear = torch.nn.Linear(4096, 8)
 
    def forward(self, x):
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.layer1(out)
        out = self.conv2(out)
        out = self.bn2(out)
        out = self.layer2(out)
        out = torch.flatten(out, 1)  # Flatten the output to a dimension of size 4096
        out = self.dropout(out)
        out = self.linear(out)
        return out


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
