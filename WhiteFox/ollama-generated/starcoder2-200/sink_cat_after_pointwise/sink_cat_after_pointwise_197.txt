
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0)  # Concatenate two input tensors along the first dimension. The resulting tensor has 3 dimensions: batch_size X 10 X 5
        t2 = t1[:, :, :]
        v2 = F.relu(t2[:, 4, :])

        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3, 10) # x1 is of size batch_size X 10 and is used as input tensor in the forward method
x2 = torch.randn(3, 5)   # x2 is of size batch_size X 5 and also used as input tensor in the forward method


# Outputs from the model
__output___0  = m(x1, x2).shape == [3, 4]    # The output shape should be [batch_size, 4]. Otherwise, sinking failed.
__output___1  = m(x1, x2)[m(x1, x2) < torch.tensor(0)].size() == [3, ] # There should not exist negative elements in the output of the model. Otherwise, sinking failed.

