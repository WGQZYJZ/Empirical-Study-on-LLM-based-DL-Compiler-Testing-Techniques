
class Model(torch.nn.Module):
    def __init__(self, dim=512):
        super().__init__()
        self.linear1 = torch.nn.Linear(in_features=dim, out_features=dim // 8)
        self.linear2 = torch.nn.Linear(in_features=dim // 8, out_features=dim // 4)
        self.linear3 = torch.nn.Linear(in_features=dim // 4, out_features=dim // 2)
        self.linear4 = torch.nn.Linear(in_features=dim // 2, out_features=dim)
        self.linear5 = torch.nn.Linear(in_features=dim, out_features=1)
 
    def forward(self, input):
        x = F.relu(self.linear1(input))
        x = F.relu(self.linear2(x))
        x = F.relu(self.linear3(x))
        x = F.relu(self.linear4(x))
        x = self.linear5(x)
        return x


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(1, 64, 64, 3)
