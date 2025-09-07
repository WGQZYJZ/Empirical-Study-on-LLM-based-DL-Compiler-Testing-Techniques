
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_A = torch.nn.Linear(2, 2)
        self.linear_B = torch.nn.Linear(1, 1)

    def forward(self, x1, x2):
        t1 = x1.permute(0, 2, 1)
        v2 = torch.bmm(t1, input_tensor_A)
        t3 = x2.permute(0, 2, 1)
        return self.linear_B(torch.bmm(t2, input_tensor_B))


# Initializing the model
m = Model()


