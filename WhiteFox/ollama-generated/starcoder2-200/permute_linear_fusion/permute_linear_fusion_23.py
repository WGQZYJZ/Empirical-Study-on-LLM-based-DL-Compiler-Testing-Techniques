
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         t1 = torch.randn(2, 3)
         t2 = torch.nn.functional.linear(t1[:, 0], self.linear.weight[0][0])
         return v2

# Initializing the model
m = Model()

