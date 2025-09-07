
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0 = torch.rand((2,), dtype=x1.dtype)

        # Permute and re-apply the linear layer on the permuted input tensor
        v1  = v0.view(v0.shape[0], -1).permute(0, 1) + x1

        # Apply linear transformation to the permuted input tensors with different weight and bias vectors.
        v2 = torch.nn.functional.linear(x=v1,
                                        weight=(torch.rand((4, 3), dtype=x1.dtype),),
                                        bias=(torch.rand((5,), dtype=x1.dtype),))

        # Apply softmax to the permuted input tensors
        v2 = torch.nn.functional.softmax(input=v1) + x1

        return (v0, v1, v2)


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(3, 4, dtype=torch.float64)
__output__,  __output_0__, __output_1__,   __output_2__  = m(x1)

