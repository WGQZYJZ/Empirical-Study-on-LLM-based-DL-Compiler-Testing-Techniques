
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensor_1 = torch.split(x1, [256], dim=1)
        return self.conv(split_tensor_1[0]) + self.conv(split_tensor_1[1])

# Initializing the model
m = Model()
