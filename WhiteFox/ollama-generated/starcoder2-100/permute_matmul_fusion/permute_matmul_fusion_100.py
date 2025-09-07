
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)
        self.linear2 = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = torch.bmm(x1.permute(0, 2, 1),
                        (self.linear1 + self.linear2).weight) + self.linear1.bias

        v2 = torch.matmul(x2.permute(0, 3, 2, 1),
                          x1.transpose(0, -2))
        v3 = torch.bmm(v2,
                        ((self.linear1 + self.linear2).weight).permute(0, 2,
                                                                        1))

        v4 = (x2.reshape(
            (
                -(len(input_tensor_shape_list_1) - input_tensor_rank),
                1
            )
        ) * torch.nn.functional.sigmoid(v3)).transpose(0, 2).sum(dim=(-1))

        return v4

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(10, 5)
x2  = torch.randn(10, 3)
__output__  = m(x1, x2)
