
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.nn.functional.linear(x1, self.weight, self.bias)


m = Model()

x1  = torch.randn(1, 2, 4, 3) # input_tensor is rank 5, output_tensor is rank 3
