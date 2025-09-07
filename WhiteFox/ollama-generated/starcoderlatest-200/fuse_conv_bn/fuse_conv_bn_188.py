
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        output = torch.nn.functional.conv2d(x1, w)
        output = torch.nn.functional.batch_norm(output)
        return output


# Initializing the model
m = Model()

