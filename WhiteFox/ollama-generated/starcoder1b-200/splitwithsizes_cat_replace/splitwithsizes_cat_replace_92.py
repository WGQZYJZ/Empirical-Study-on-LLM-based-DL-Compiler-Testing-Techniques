
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        x1_splitted = torch.split(x1, [64, 64], dim=0)
        concatenated_tensor = torch.cat([input_tensor for input_tensor in x1_splitted])
        return concatenated_tensor

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
