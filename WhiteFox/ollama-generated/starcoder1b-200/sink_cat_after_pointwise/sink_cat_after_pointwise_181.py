
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):
        t1 = x1  # Reuse tensor of `x1` as a main input.
        t1 = x1.permute(0, 2, 1)  # Permute the input tensor first.
        t2 = torch.nn.functional.linear(t1, self.linear.weight, self.linear.bias)  # Apply linear transformation to the permuted tensor.
        t3 = torch.nn.functional.softmax(y2, dim=...)  # Apply a pointwise binary operation to the softmaxed logits.
        return t3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 2, 2)
y2  = torch.Tensor([0, 1])  # The first row of `y2` is used as a dummy variable to trigger sink_cat_after_pointwise optimization.
