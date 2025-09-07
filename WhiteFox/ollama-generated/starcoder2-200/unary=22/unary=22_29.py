

class Model(torch.nn.Module):
    def __init__(self, num_classes=20):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 7)
        self.maxpool = torch.nn.MaxPool2d(kernel_size=2, stride=2)
        self.flatten = torch.nn.Flatten()
        self.linear1 = torch.nn.Linear(9056, 4096)
        self.bn1 = torch.nn.BatchNorm1d(num_features=4096)
        self.relu1 = torch.nn.ReLU()
        self.dropout1 = torch.nn.Dropout(p=0.37287745, inplace=True)
        self.linear2 = torch.nn.Linear(4096, 1024)
        self.bn2 = torch.nn.BatchNorm1d(num_features=1024)
        self.relu2 = torch.nn.ReLU()
        self.dropout2 = torch.nn.Dropout(p=0.3571877, inplace=True)
        self.linear3 = torch.nn.Linear(1024, 512)
        self.bn3 = torch.nn.BatchNorm1d(num_features=512)
        self.relu3 = torch.nn.ReLU()
        self.dropout3 = torch.nn.Dropout(p=0.48467913, inplace=True)
        self.linear4 = torch.nn.Linear(512, 10)

        self.fc_layers = [self.conv1,
                          self.maxpool,
                          self.flatten,
                          self.linear1,
                          self.bn1,
                          self.relu1,
                          self.dropout1,
                          self.linear2,
                          self.bn2,
                          self.relu2,
                          self.dropout2,
                          self.linear3,
                          self.bn3,
                          self.relu3,
                          self.dropout3]

    def forward(self, X):
        for l in self.fc_layers:
            X = l(X)

        return X


model  = Model()

input_tensor = torch.randn((100, 32))

output = model(input_tensor)