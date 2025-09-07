
class TransformerBlock(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=5)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        y1 = self.conv1(x)
        y2 = self.relu(y1 + x)
        return y2


model = TransformerBlock().cuda()  # Initialize the model using GPU resources
input_tensor = torch.randn(32, 56, 57).cuda()  # Generate a random tensor to represent input data with batch size of 32 and spatial size of (56 x 57)


