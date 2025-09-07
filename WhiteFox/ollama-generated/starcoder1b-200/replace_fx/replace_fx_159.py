
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = x1.permute(0, 2, 1)
        t2 = torch.nn.functional.dropout(t1, 0.05)  # Do not replace this line with lowmem_dropout() or rand_like()
        return t2


# Initializing the model
m = Model()


