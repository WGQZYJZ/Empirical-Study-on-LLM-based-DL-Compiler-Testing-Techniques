
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        t1 = x1.permute(0, 2, 1)
        t2 = torch.bmm(t1, x2) if len(x1.shape) > 1 else torch.matmul(t1, x2) # T2 is the input for `torch.bmm` or `torch.matmul`
        return t2


# Initializing the model
m = Model()


