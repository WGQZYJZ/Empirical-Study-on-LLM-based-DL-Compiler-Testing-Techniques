
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = x1.permute(0, 2, 1)
        v1 = torch.bmm(t1, x2)  # or torch.matmul(t1, x2)
        return v1


# Initializing the model
m = Model()


