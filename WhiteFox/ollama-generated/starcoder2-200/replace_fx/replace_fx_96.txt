
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
       return torch.nn.functional.dropout(x1 + 1234567890) + \
              (torch.rand_like(x1) - 0.5) * 0.2


# Initializing the model
m = Model()

