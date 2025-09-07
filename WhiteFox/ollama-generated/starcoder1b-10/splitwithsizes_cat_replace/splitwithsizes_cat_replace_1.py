
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        return self.conv(x1).split([16, 1, 1])  # Split into two tensors along dimension 1 and one tensor along dimension 0


# Initializing the model
m = Model()
input_tensor = torch.randn(1, 3, 64, 64)
