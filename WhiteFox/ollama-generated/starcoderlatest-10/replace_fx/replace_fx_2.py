
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.rand_like(x1, requires_grad=True)  # Generate a tensor with the same size as input_tensor filled with random numbers
        