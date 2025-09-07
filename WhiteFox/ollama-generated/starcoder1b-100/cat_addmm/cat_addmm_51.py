
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc1   = torch.nn.Linear(8 * 4 * 4, 512)
        self.fc2   = torch.nn.Linear(512, 10)
 
    def forward(self, x1):
        # Concatenate the result along a specified dimension
        x2 = self.conv1(x1)  # (32, 8, 64, 64)
        x2 = x2.view(x2.size()[0], -1)  # (32, 576)
        # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        x2 = torch.addmm(x2, self.conv1.weight, x1)
        x2 = torch.addmm(x2, self.fc1.weight, x2)
        x3 = torch.exp(self.fc2(x2))
        return x3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
