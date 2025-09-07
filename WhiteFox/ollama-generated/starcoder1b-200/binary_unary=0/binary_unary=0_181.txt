
class Model(torch.nn.Module):
    def __init__(self, num_layers):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.layer1 = torch.nn.ModuleList()
        for _ in range(num_layers):
            self.layer1.append(torch.nn.Linear(8, 5))
        self.conv2 = torch.nn.Conv2d(5, 8, 1, stride=1, padding=1)
        self.layer2 = torch.nn.ModuleList()
        for _ in range(num_layers):
            self.layer2.append(torch.nn.Linear(8, 5))
 
    def forward(self, x1):
        v1 = self.conv1(x1)
 
        # Apply layers
        for layer in self.layer1:
            v1 = torch.relu(layer(v1))
 
        v2 = v1 + other
        v3 = torch.relu(t2)
        return v3


# Initializing the model
m = Model()


