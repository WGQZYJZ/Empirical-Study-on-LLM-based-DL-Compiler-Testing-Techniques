
class Model(torch.nn.Module):
    def __init__(self, n1=2, n2=3):
        super().__init__()
        self.n1 = n1
        self.n2 = n2

    def forward(self, x1):
        v1  = torch.cat([x1] * self.n2, dim=-1) # Concatenate the input tensor along a dimension with an equal amount of copies. This operation is the main user of the tensor for which this sink pattern is triggered.
        v2  = v1.view(v1.size()[0], -1) # Reshape the concatenated tensors.
        v3  = torch.relu(v2) # Apply ReLU to each value in the reshaped tensor.
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 3)
__output__  = m(x1)

# A more complex example: ReLU to a tensor with many dimensions
class Model(torch.nn.Module):
    def __init__(self, n=2):
        super().__init__()

        self.linear_1 = torch.nn.Linear(n, n+3).cuda()

    def forward(self, x0):
        # Concatenate two input tensors along dimension 2 after permuting one of them. The concatenated tensor should have many dimensions to satisfy the sink pattern.
        v1  = self.linear_1(torch.nn.functional.relu(x0.permute([0, 2, 1]))).cuda()

        return torch.nn.functional.softmax(v1)
m  = Model(3459786) # This model will be used as input for sink_cat_after_pointwise.

# Input to the model
x0 = torch.randn(2, 3).cuda() # Note that the reshaped tensor has more than two dimensions here so it is a good candidate of sink pattern

# Output from the model
