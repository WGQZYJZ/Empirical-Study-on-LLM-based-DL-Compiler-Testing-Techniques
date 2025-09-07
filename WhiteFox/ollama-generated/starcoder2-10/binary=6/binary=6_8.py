
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.randn(64)
        v2  = torch.randn(30000)

        v1_out  = F.relu(x1 + v1) # Adding 1 to the output of the linear transformation and applying the ReLU function
        v2_out  = self._add_other(v1, x2, v2) # Adding 'other' to a tensor and subtracting it from another tensor
        return torch.abs(x1 + x2)


# Initializing the model
m = Model()

# Inputs to the model