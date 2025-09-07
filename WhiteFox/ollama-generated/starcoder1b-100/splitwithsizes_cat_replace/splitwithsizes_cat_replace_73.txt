
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.split_sizes = [7]
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = split_tensor[i] * 0.5
        return True if len(v3) == 0 else False

 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
