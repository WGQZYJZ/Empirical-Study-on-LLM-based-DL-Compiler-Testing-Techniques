
class Model(torch.nn.Module):
    def __init__(self, hidden_channels=16):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.linear1 = torch.nn.Linear(14*14*8, hidden_channels)
        self.linear2 = torch.nn.Linear(hidden_channels, hidden_channels // 2)
        self.linear3 = torch.nn.Linear(hidden_channels // 2, 10)
 
    def forward(self, x):
        t1 = torch.addmm(x.view(-1, 14*14*8), self.linear1.weight, self.linear1.bias)
        t2 = torch.cat([t1], dim=1) # Concatenate the result along dimension 1 to match the dimension of mat2 (dimension 0 will not change)
        t3 = torch.nn.functional.relu(self.linear2(t2))
        t4 = self.linear3(t3)
        return t4


# Initializing the model
m = Model()

