
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(20, 8)
        self.fc2 = torch.nn.Linear(8, 4)

    def forward(self, x1, x2):
        v1 = self.fc1(x1)
        v2 = self.fc2(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(3, 50)
t1 = m.fc1(input_tensor)
t2 = t1 * 2 + 1
t3 = t1 * 1000 + 1
t4 = torch.erf(t3)
t5 = t4 + 1
t6 = t2 * t5
