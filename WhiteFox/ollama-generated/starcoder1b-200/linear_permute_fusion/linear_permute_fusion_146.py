
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(input_tensor, self.linear.weight, self.linear.bias)
        return v1


# Initializing the model
m  = Model()

