
class Model(torch.nn.Module):
    def __init__(self, n, m):
        super().__init__()

        self._n = n # 1
        self._m = m # 2

        self.linear1 = torch.nn.Linear(4 * n + m, 5)
        self.linear2 = torch.nn.Linear(5, 3)

    def forward(self):
        l0 = F.relu(self.linear1())
        l1 = F.relu(torch.cat([l0] * self._m))

        l1_out = l1.reshape(-1)
        l2 = F.sigmoid(self.linear2(l1_out))

    def run(self): # 3
        x1, x2 = self._n, self._m
        m  = torch.nn.Linear(x1 * (4 + x2), 5)

        l0 = F.relu(m())
        l1 = F.relu(torch.cat([l0] * x2))
        return l1

# Initializing the model
m  = Model(1, 2) # 4

# Input to the model
input_tensor = torch.randn(3, 4*1 + 2*2)


# Expected result of execution: 3
