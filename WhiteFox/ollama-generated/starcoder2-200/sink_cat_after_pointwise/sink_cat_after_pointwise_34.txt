
class Model(torch.nn.Module):
    def __init__(self, hidden1=32, hidden2=40):
        super().__init__()

        self._linear = torch.nn.Linear(8, 9)

    def forward(self, t1, t2):
        v1 = t1 + t2
        v2 = torch.cat([v1, t1], dim=-1)
        v3 = v2 / 5

        return self._linear(v3), v1


# Initializing the model
m = Model()


# Inputs to the model
t1 = torch.rand(8, 4, dtype=torch.float64) + 0j
t2 = torch.rand(9, 7).double().normal_(-3., .5) * (-np.pi / 3.) ** 1e-2

 