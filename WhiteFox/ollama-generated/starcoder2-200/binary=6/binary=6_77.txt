
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 10)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 - other # 'other' is a tensor or scalar of shape [1, 1]
        return v2


# Initializing the model
m2 = Model()


