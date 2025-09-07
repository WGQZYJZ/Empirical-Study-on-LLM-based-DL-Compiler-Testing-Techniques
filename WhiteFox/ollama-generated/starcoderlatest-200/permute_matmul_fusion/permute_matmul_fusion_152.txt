
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bmm1 = torch.nn.Bilinear(2, 2, 2)
        self.bmm2 = torch.nn.Bilinear(2, 3, 4)

    def forward(self, x1, x2):
        v1 = input_tensor_A.permute(0, 2, 1)
        v2 = input_tensor_B.permute(0, 1, 2)
        v3 = torch.bmm(v1, v2)
        return torch.matmul(x1, self.linear(input_tensor_A))


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 4, 3)
