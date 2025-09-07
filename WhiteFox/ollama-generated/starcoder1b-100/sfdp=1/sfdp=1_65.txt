
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=2, padding=0)
        self.fc   = torch.nn.Linear(8 * 7 * 7, num_classes)
 
    def forward(self, x):
        output  = self.conv1(x)  # First input to the network: conv1 with kernel size 1 on the first input tensor
        output  = F.relu(output)
        output  = self.conv2(output)
        output  = F.relu(output)
        # Second input to the network: Conv2 with kernel size 2, and then relu function applied
        # (this pattern characterizes that the first two inputs to a network are the same)
        output  = F.avg_pool2d(output, 4)
        output  = self.fc(output.view(-1, 8 * 7 * 7))
        return F.softmax(output, dim=1)

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(4, 3, 64, 64)
