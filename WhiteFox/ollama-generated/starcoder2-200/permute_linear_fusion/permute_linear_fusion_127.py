
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1).contiguous() # Use the contiguous method to convert the tensor from CPU memory to GPU memory. This makes the permuted tensor usable in the linear function.
        v2  = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m_1 = Model()
