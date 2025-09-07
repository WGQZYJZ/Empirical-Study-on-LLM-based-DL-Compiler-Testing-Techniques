
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.rand_like(x1, dtype=x1.dtype)
        t1 = torch.nn.functional.dropout(v1, p=0.25) # Using lowmem dropout
        v2 = torch.rand_like(input_tensor, ...)
        return torch.nn.functional.linear(t2, self.linear.weight, self.linear.bias)
# Initializing the model
m = Model()

