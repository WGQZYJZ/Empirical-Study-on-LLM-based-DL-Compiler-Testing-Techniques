
class Model(torch.nn.Module):
    def __init__(self, num_input_tensors: int = 3):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(num_input_tensors, 8, 1)
        self.conv2 = torch.nn.Conv2d(num_input_tensors, 16, 1)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(x)
        return torch.cat([v1, v2], dim=1)


# Initializing the model
m = Model()

