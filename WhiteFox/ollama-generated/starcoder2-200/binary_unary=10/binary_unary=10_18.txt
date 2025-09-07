
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1024 * 3, 7)

    def forward(self, x):
        t1  = self.linear(x)
        t2  = t1 + other_tensor  # Some existing tensor here
        t3  = F.relu(t2)
        return t3
# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(50, 8 * 3)
__output__  = m(x1)

- - - 
