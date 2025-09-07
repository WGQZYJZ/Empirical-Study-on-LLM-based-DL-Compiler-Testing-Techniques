
class Model(torch.nn.Module):
    def __init__(self, hidden_dim: int):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 3, stride=2, padding=1)
        self.fc1   = torch.nn.Linear(hidden_dim, hidden_dim//2)
        self.fc2   = torch.nn.Linear(hidden_dim//2, hidden_dim)
 
    def forward(self, x1: torch.Tensor):
        v1 = self.conv1(x1)  # [batchSize, channelDim, height, width]
        v2 = self.conv2(v1)  # [batchSize, channelDim*2, height/2, width/2]
        v3 = v2.flatten()  # [batchSize * (channelDim*2), height*width]
        v4 = v3.view(v3.size(0), -1)  # [batchSize * channelDim * height * width]
        return self.fc1(v4).relu().view(-1, v4.shape[1]) + self.fc2(v4)


# Initializing the model
m = Model(hidden_dim=64)


