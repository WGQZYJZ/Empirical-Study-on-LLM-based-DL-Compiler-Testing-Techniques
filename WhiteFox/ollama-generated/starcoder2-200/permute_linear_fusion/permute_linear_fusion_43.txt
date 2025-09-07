
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 10)

    def forward(self, x1):

        # This line is used to prevent grads from being accumulated on the permuted tensors
        with torch.no_grad():
            v1  = input_tensor.permute(0, 2, 1).requires_grad_(True)
        v3 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)

        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(2, 4, 2)

# Targets for the model on the inputs

target1_1  = x1[0, -5:, :].mean().reshape(-1).item() + torch.rand([8]).sum().item() # For example

# Actual outputs of the model from the inputs to get the expected targets (If there are multiple expected targets that can be produced by the same input)

output_target1 = m(x1, target1_1)

