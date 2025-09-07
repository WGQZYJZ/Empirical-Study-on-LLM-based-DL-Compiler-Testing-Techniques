
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.conv2d(input_tensor, weight)
        v = torch.nn.functional.batch_norm(v)
        return v


# Initializing the model
m = Model()


