
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 3, 1).contiguous() # Replace contiguous with permute to generate the same tensor shape in PyTorch v1.4.0 (torch_nightly-1.5.0_20200617)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 2, 3).permute(0, 1, 3, 2).contiguous().view(-1, 4)
