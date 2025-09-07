
class Model(torch.nn.Module):
    def __init__(self, input_tensor):
        super().__init__()
        self.conv = torch.nn.Conv2d(input_tensor, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1) + x2
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model(3)


