
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=0)
        self.fc1 = torch.nn.Linear(16 * 7 * 7, 10)
        self.dropout = torch.nn.Dropout2d()
 
    def forward(self, x):
        v1 = self.conv1(x)
        # [batch_size, 8, height_size//4, width_size//4]
        v2 = self.conv2(v1).view(-1, 16 * 7 * 7)
        # [batch_size, 10]
        m = v2.matmul(self.dropout(self.fc1(v2)))  # [batch_size, 10]
        return m


# Initializing the model
m = Model()

