
class Model(torch.nn.Module):
    def __init__(self, device: Device):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
        self.device = device

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)  # Permute the input tensor
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias).to(
            self.device)  # Apply linear transformation to the permuted tensor

        return v2


# Inputs to the model
x1 = torch.randn(1, 2, 3).to("cuda")  # Input tensor with 3 dimensions
