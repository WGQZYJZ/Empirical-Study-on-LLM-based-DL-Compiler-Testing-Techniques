
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc1 = torch.nn.Linear(8 * 64 * 64, 8 * 1024)
        self.dropout1 = torch.nn.Dropout(0.5)
        self.conv2 = torch.nn.Conv2d(3, 16, 1, stride=1, padding=1)
        self.fc2 = torch.nn.Linear(8 * 1024, 8 * 2048)
        self.dropout2 = torch.nn.Dropout(0.5)
        self.conv3 = torch.nn.Conv2d(16, 32, 1, stride=1, padding=1)
        self.fc3 = torch.nn.Linear(8 * 2048, 10)
 
    def forward(self, x):
        # Batch Normalization
        x = self.dropout1(F.batch_norm(
            self.conv1(x), (x.shape[0], x.shape[1]), False, True))
 
        # Pointwise Convolution and Residual Connections
        v = self.conv2(self.dropout1(x))
        x = F.relu(self.fc1(v))
 
        # Batch Normalization
        v = self.conv3(F.relu(self.fc2(self.dropout1(x))))
 
        return self.fc3(F.log_softmax(v, dim=-1))


# Initializing the model
m = Model()

