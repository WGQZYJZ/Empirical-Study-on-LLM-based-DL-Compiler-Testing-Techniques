
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.rand_like(x1)  # generate a random tensor of the same shape as 'v1' in the code below
        v1 = torch.tensor([0., 1.], dtype=torch.float32).reshape(-1, 1, 2) * x1 + v1   # scale and shift the tensor to get two additional dimensions, then permute it
        v1 = self.linear(v1)

        return v1
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
