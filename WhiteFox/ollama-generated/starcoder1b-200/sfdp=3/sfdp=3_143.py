
class Model(torch.nn.Module):
    def __init__(self, dim_model=64):
        super().__init__()
        self.dim = dim_model
        self.fc1  = torch.nn.Linear(7 * 7 * dim_model, 300)
        self.fc2  = torch.nn.Linear(300, 100)
        self.fc3  = torch.nn.Linear(100, 50)
        self.fc4  = torch.nn.Linear(50, 50)
        self.fc5  = torch.nn.Linear(50, dim_model)
 
    def forward(self, x):
        x = x.view(-1, 7 * 7 * self.dim)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, p=self.drop)
        x = F.relu(self.fc2(x))
        x = F.dropout(x, p=self.drop)
        x = F.relu(self.fc3(x))
        x = F.dropout(x, p=self.drop)
        x = F.relu(self.fc4(x))
        x = F.dropout(x, p=self.drop)
        x = self.fc5(x)
        return x


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(1, 7 * 7 * 64)
