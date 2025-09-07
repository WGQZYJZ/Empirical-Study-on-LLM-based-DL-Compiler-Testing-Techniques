
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):  # Input tensors with more than 2 dimensions cannot be directly used as the main inputs for these functions, because of the fact that both input tensors are swapped with each other before being passed to them
        v1 = x1.permute(0, 2, 1)
        v2 = torch.bmm(v1, x2)
        return v2


# Initializing the model
m = Model()


