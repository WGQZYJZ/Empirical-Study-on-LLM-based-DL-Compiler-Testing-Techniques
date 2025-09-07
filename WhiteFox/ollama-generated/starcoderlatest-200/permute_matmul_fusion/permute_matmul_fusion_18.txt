
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # Permute the first input tensor.
        v2 = x2.permute(0, 2, 1) # Permute the second input tensor.
        output_tensor = torch.nn.functional.linear(v1, self.linear1.weight, self.linear1.bias) \
                        + torch.nn.functional.linear(v2, self.linear2.weight, self.linear2.bias)
        return output_tensor


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
