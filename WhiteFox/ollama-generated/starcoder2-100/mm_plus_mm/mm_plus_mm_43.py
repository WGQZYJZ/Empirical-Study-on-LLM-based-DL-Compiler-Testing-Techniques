
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # input1
        input2 = torch.randn((3457890, 3))
        input3 = torch.randn((6578344, 3457890))
        input4 = torch.randn((6578344, 3))

        return torch.mm(input1, x1) + \
            torch.mm(x1, input2)


# Initializing the model