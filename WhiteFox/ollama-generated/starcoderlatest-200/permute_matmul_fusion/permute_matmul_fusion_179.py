
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = input_tensor_A.permute(0, 2, 1)
        v2 = input_tensor_B.permute(0, 2, 1)
        t3 = torch.bmm(v1, v2)
        t4 = torch.matmul(x1, x2)
        return (t1 + t2), t3


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
__output_A__, __output_B__ = m(x1, x2)

