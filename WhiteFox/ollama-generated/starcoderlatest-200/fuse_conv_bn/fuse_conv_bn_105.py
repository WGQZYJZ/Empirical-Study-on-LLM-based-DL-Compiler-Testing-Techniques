
class Model(torch.nn.Module):
    def __init__(self, x1):
        super().__init__()

    def forward(self, x2):
        output = torch.nn.functional.batch_norm(torch.nn.functional.conv2d(x1, weight), gamma, beta)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 4, 4)
x2 = torch.randn(1, 3, 4, 4)
