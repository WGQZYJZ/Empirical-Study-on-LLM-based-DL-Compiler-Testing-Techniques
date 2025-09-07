
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        t1 = x1.permute(0, 2, 1)
        t2 = torch.bmm(t1, x2) # or torch.matmul(t1, input_tensor_B)
        return t2


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 3, 2)
