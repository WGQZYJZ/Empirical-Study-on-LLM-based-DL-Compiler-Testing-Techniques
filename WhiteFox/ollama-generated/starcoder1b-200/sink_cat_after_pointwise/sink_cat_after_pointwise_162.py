
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @sink_cat_after_pointwise()
    def forward(self, x1, x2):
        return torch.relu(x2)  # Relu on the concatenated tensor


# Inputs to the model
x1 = ...
x2 = ...
