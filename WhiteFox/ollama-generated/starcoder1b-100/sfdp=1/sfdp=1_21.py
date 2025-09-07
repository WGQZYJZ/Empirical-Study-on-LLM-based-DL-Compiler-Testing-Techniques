
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1d  = torch.nn.Conv1d(3, 8, 5)
        self.conv2d  = torch.nn.Conv2d(3, 8, 3)
 
    def forward(self, x1):
        v1 = F.conv1d(x1, kernel_size=5, stride=1, padding=2) # Conv1D
        v2 = F.conv2d(v1, kernel_size=(3, 3), stride=(1, 2), padding=(1, 0)) # Conv2D
        return torch.max(x1 * x2, dim=-1)[0]  # Apply max on the outputs of the two convolutions


# Initializing the model
m = Model()


