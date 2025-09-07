
class Model(torch.nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.fc1 = torch.nn.Linear(32*64*64, 256)
        self.fc2 = torch.nn.Linear(256, num_classes)
 
    def forward(self, x):
        x = x.view(x.shape[0], -1)
        x = F.relu(self.fc1(x))
        x = F.softmax(self.fc2(x), dim=1)
        return x

# Initializing the model
m = Model()


