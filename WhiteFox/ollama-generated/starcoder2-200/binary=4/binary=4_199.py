
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, other):
        v1 = torch.nn.functional.linear(x1)  # Apply a linear transformation to the input tensor
        v2 = v1 + other  # Add another tensor (specified by keyword argument "other") to the output of the linear transformation
        return v2


# Initializing the model and setting "other" as some tensor (e.g., torch.zeros(3,3))
m = Model()
other_tensor  = torch.zeros(3, 3)

 # Inputs to the model with the input tensors of size [1,4] and [2, 5]:
x1 = torch.randn(1, 4)
y1  = m(x1, other=other_tensor)
 
x2  = torch.randn(3, 5)
y2  = m(x2, other=other_tensor)

 