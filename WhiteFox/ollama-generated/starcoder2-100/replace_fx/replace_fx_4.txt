
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.rand_like(x1, dtype=torch.float32)  # Generate a tensor with the same size as input_tensor filled with random numbers
        v1  = x1.mul(v2).clamp_(0., 5.) + self.weight  # Apply multiplication and clamping to input_tensor. This operation is then used as the main input for the linear function
        return torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)


# Initializing the model
m = Model()


# Inputs to the model
x2  = torch.randn(30, 80, 50)


__output__  = m(x2)