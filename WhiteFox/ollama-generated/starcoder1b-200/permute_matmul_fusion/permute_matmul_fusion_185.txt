
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.bmm(v1, input_tensor_B)
        v3 = torch.matmul(input_tensor_A, t1)
        return self.linear2(self.linear1(t2))


# Initializing the model
m = Model()


