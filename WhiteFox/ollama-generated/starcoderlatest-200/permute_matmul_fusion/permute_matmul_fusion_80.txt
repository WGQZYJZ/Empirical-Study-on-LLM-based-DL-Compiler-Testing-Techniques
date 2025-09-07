
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1).contiguous() # This operation is only required when input_tensor_A has more than 2 dimensions
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        