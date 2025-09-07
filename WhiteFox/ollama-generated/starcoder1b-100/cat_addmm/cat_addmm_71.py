
class Model(torch.nn.Module):
    def __init__(self, input_size=(100)):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc   = torch.nn.Linear(input_size, 5)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.7071067811865476
        v3 = self.fc(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
input = torch.randn((2, 3, 100))  # Shape: [batch_size, input_width, input_height]
