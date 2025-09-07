
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(100, 8)
 
    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = torch.nn.functional.relu(v1)
        return v2


# Initializing the model
m2 = Model2()


