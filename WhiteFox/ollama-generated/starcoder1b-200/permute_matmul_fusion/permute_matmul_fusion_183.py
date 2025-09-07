
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1  = x1.permute(0, 2, 1)
        v2  = torch.bmm(v1, input_tensor_A)  # or torch.matmul(v1, input_tensor_A)
        return v2


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 4)
x2 = torch.randn(3, 3, 5)
