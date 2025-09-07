
class Model(torch.nn.Module):
    def __init__(self, A, B):
        super().__init__()

        self.linearA = torch.nn.Linear(2, 4)
        self.linearB = torch.nn.Linear(3, 5)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1).matmul(x2)
        v2 = x1.permute(0, 2, 1).bmm(x2)

        return self.linearA(v1), \
               torch.nn.functional.linear(v2,
                                           self.linearB.weight[None, :],
                                           self.linearB.bias)


# Initializing the model
m = Model(input_tensor=torch.randn(3, 4, 2))

# Inputs to the model
x1 = torch.randn(50000, 8096 * 3)
x2 = torch.randn(7932, 4, 8096)


