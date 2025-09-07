
class Model(torch.nn.Module):
    def __init__(self, input_tensor):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
        self.input_tensor = input_tensor

    def forward(self):
        return torch.cat([
            self.input_tensor.view((1, -1)),
            torch.nn.functional.linear(
                self.input_tensor.view((1, -1)),
                self.linear.weight,
                self.linear.bias))])


# Inputs to the model
x1 = torch.randn(1, 2)
