
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.rand_like(input_tensor, 0) # Apply random_like to input tensor
        v2 = torch.nn.functional.dropout(x1, self.linear.weight, self.linear.bias) # Apply dropout to the input tensor
        return v2


# Inputs to the model
x1 = torch.randn(1, 2, 2)
