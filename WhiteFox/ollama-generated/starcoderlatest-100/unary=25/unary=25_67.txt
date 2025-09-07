
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0).type_as(x1) # Note that the type of the boolean tensor and the output of linear transformation is same, and it has to be converted into a tensor because the elementwise product function only works with tensors
        v3 = v1 * -0.01
        v4 = torch.where(v2, v1, v3) # Note that the shape of boolean tensor matches with shape of negative slope, otherwise an error is generated (which indicates a bug in model code generation), and we do not implement where operation for Boolean tensors yet.
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
