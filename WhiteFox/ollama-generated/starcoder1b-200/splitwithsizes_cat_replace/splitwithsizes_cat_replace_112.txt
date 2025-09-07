
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.split_tensor1 = [
            torch.randn(1, 3, 64, 64),
            torch.randn(1, 3, 64, 64),
        ]
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2_0, v2_1 = self.split_tensor1
        return v1 + v2_0


# Initializing the model
m = Model()


