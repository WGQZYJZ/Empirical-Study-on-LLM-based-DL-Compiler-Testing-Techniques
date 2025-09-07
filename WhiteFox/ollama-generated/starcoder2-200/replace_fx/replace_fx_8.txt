
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t3 = self.linear(x1) # Linear transformation with input size [N, 2] and output size [N, 4].
        t1 = torch.nn.functional.dropout(t3, ...) # Apply dropout to the transformed tensor with probability of dropping out being set as 0.8.
        t2 = torch.rand_like(t3, ...) # Generate a random input that has similar shape and size of `t3`.
        return t1, t2

# Initializing the model
m = Model()


# Inputs to the model:
x1  = torch.randn(8, 2)
__output__  = m(x1)
