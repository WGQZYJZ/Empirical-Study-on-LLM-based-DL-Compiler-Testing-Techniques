
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        output = []
        for i in range(5):
            input_i = torch.randn(64, 64)
            input_j = torch.randn(64, 64)
            output.append(torch.mm(input_i, input_j))
        return torch.cat(output, dim=0)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
