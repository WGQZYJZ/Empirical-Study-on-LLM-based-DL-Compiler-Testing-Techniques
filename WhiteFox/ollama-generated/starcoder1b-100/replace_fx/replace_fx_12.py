
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.lowmem_dropout(v1, p=0.25)  # Apply lowmem dropout to the permuted tensor
        v3 = torch.rand_like(v1, dtype=torch.float)  # Generate a tensor with the same size as input_tensor filled with random numbers
        v4 = self.linear(v3)
        return v4


# Initializing the model
m = Model()
