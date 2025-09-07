
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.dropout(x1, 0.5)
        return v


# Initializing the model with a random input tensor
m2 = Model2()
rand_input_tensor = torch.randn(1, 3, 3)
