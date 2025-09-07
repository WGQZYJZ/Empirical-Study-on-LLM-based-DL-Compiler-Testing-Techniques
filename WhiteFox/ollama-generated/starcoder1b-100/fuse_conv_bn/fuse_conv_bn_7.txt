
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input_tensor: torch.Tensor) -> torch.Tensor:
        conv  = torch.nn.functional.conv2d(...)
        bn    = torch.nn.functional.batch_norm(...)
        output = bn(conv(input_tensor))

        return output


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = ...  # Input tensor of a shape such as (1, 2, 2)
