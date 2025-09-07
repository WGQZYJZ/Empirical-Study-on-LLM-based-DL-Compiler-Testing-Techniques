
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 4, stride=2, padding=1)
 
    def forward(self, x):
        # Get the feature map from Conv1 and Conv2
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
 
        # Compute output after each step of the model.
        return [v1, v2]


# Initializing the model
m = Model()


