
class Model(torch.nn.Module):
    def __init__(self, in_feature, out_feature):
        super().__init__()
        self.fc1 = torch.nn.Linear(in_feature, 8)
        self.relu = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(8, out_feature)
 
    def forward(self, x):
        v1 = self.relu(self.fc1(x))
        return self.fc2(v1)


# Initializing the model
m = Model(in_feature=3, out_feature=4)


