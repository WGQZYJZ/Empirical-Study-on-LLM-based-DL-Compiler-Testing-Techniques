
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 1, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1)) # A view is a way to specify dimensions of tensors without changing the underlying shape of the tensor
        return v1


# Inputs to the model
x1 = torch.randn(2, 64 * 1, 50, 30)
