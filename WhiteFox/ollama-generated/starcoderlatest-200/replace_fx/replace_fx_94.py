
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5)  # The dropout function is invoked on the input tensor with a probability of 0.5
        v2 = torch.rand_like(v1)                        # The rand_like function is invoked on the tensor obtained by applying the dropout
        return v2


# Inputs to the model
x1 = torch.randn(1, 2, 4)
