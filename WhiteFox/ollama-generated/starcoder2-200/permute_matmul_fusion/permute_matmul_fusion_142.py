
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):  # Here, we have two input tensors
        v1 = x1.permute(0, 3, 1, 2)
        v2 = torch.bmm(y2, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model