
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(256, 4)
 
    def forward(self, x1):
        v1 = x1[:, :, :, None]  # Extract a channel-axis into a batch-axis and add it to the last dimension of the input
        v2 = v1 + 1
        v3 = self.fc1(v2)
        return v3


# Inputs to the model
x1 = torch.randn(4, 256, 10, 10)
