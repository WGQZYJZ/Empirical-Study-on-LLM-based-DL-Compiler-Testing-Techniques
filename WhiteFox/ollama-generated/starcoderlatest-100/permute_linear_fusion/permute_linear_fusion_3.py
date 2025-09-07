
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.permute(x1, 0, 2, 1)
        v2 = torch.nn.functional.linear(v1, ...)
# Please check whether the output tensor type is correct. The model should be different from the previous one.


# Inputs to the model
x1 = torch.randn(1, 2, 2)
