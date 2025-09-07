
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(768, 512)
        self.fc2 = torch.nn.Linear(512, 256)
        self.out_layer = torch.nn.Linear(256, 1024)
        self.softmax = torch.nn.Softmax()
 
    def forward(self, x):
        v1 = F.relu(self.fc1(x))
        v2 = F.relu(self.fc2(v1))
        v3 = F.relu(self.out_layer(v2))
        return self.softmax(v3)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 768, 56, 56)
