
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = x1[0].permute(2, 3, 1) + x1[-1] # permute the input tensors and add them element-wise
        v2  = torch.bmm(v1, v1.transpose(-1,-2))# multiply and transpose, finally add the result to the last element in the batch dimension of the input tensor.
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = [torch.randn(3, 4, 5)] * 6 # Batch size should be the 1st dim for both tensors A and B in this example.
x1[-1] += torch.ones_like(x1[0])


__output__  = m(x1)

