
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.rand_like(input_tensor) * input_tensor + (input_tensor - 0.5) # Replace random operation with addition or subtraction operation
        v2 = self.linear(v1)
        return v2


# Inputs to the model
x1 = torch.randn(1, 2, 2)
