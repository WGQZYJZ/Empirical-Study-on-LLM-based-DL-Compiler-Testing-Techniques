
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.pool = torch.nn.MaxPool2d(kernel_size=2)
        self.dropout = torch.nn.Dropout()
        self.fc = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        conv  = self.conv1(x1)
        pool  = self.pool(conv)
        conv2 = self.dropout(pool)
        fc    = self.fc(conv2)
        return fc


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
