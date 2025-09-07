
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 4, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1) * 0.5 + 0.7071067811865476  # Add 0.7071067811865476 to the output of conv1
        v2 = torch.tanh(v1) * 0.5 + 1  # Apply sigmoid to the output of conv1
        w1 = self.conv2(x1) * 0.5 + 0.7071067811865476  # Add 0.7071067811865476 to the output of conv2
        v3 = torch.tanh(w1) * 0.5 + 1  # Apply sigmoid to the output of conv2
        v4 = v3  * v2
        return v4


# Initializing the model
m = Model()


