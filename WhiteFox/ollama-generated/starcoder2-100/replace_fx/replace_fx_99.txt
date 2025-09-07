
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        return torch.nn.functional.dropout(x1, 0.3),\
            torch.rand_like(x1, requires_grad=False)

# Initializing the model
m = Model()

