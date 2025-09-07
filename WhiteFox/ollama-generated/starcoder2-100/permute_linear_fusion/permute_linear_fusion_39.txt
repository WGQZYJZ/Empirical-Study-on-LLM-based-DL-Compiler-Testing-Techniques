
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # We have added self.linear.weight and self.linear.bias as attributes of this class model
        v1 = x1.permute(0, 2, 1)

# Initializing the model
m  = Model()

