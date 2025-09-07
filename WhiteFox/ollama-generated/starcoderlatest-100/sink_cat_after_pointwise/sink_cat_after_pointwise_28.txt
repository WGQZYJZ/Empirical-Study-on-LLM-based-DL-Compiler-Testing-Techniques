
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x):
        # Concatenate two tensors along axis 1, and view it to a vector
        v1 = torch.cat([x[0].view(-1, 1), x[1]], dim=1).view(-1)
        v2 = self.linear(v1)
        return v2


# Inputs to the model
input_tensor1 = torch.randn(2, 2, 2)
input_tensor2 = torch.randn(3, 2, 2)
