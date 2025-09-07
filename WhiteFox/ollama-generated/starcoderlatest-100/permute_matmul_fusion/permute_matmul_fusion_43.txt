
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_A = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = input_tensor_B.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear_A.weight, self.linear_A.bias)
        return v2
