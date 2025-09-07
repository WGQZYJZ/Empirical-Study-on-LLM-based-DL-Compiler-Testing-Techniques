
class Model(torch.nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 8, 1)
        self.fc = torch.nn.Linear(4096, num_classes)
 
    def forward(self, x1):
        v1  = self.conv1(x1)
        v2 = torch.addmm(v1, self.weight, self.bias)
        v3 = v2.view(-1, 8 * 4 * 4)
        return self.fc(v3)


# Inputs to the model
x1 = torch.randn(1, 1, 64, 64)
