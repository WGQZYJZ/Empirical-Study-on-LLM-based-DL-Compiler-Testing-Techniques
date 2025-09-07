
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 1)

    def forward(self, x1):
        t1  = input_tensor.permute(...) # permute
        v2 = torch.nn.functional.linear(t1, self.linear.weight, self.linear.bias)

        return v2

# Initializing the model