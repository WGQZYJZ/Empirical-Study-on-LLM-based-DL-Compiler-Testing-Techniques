
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 4, 1) # Batch size = batch_size of input
        self.conv2 = torch.nn.Conv2d(4, 8, 1, stride=2) # Batch size = batch_size * height * width
    def forward(self, x):
        v = torch.mm(x, torch.mm(x, self.conv1)) + torch.mm(x, torch.mm(x, self.conv2))
        return v

# Initializing the model
m = Model()

