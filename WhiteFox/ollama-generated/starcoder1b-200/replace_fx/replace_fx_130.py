
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        # Use `torch.rand_like` to generate a tensor with the same size as input_tensor filled with random numbers
        v2 = torch.rand_like(x1, dtype=torch.float32, device='cuda:0')  # Generate a random number for a given shape and device

        v1 = x1.permute(0, 2, 1)
        v3 = self.linear(v1).contiguous()  # `contiguous` can be removed after this pattern characterizes scenarios where the input is already contiguous and we don't want to generate it again with `torch.rand_like`.

        return v3


# Inputs to the model
x1 = torch.randn(1, 2, 2)
