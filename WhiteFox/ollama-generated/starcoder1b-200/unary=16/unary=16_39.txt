
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(16 * 25, 40)
 
    def forward(self, x1):
        v1 = self.conv(x1).view(-1, 16, 25) # Unfold the input tensor into (batch_size, num_filters) shape
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model()

