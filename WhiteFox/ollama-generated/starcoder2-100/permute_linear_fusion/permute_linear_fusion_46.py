
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = input_tensor.permute(0, 3, 4, 5, 6, ..., 7).contiguous() # Add 'contiguous' method after the permute method invocation
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model