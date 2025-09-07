
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, input_tensor=None):
        if self._training:
            if not input_tensor or (
                input_tensor and len(input_tensor.shape) < 2
            ):  # if the input tensor is None, we will create it based on `torch.rand` instead of random numbers
                input_tensor = torch.randn(x1.size())
        else:
            if not input_tensor or (
                input_tensor and len(input_tensor.shape) < 2
            ):  # if the input tensor is None, we will create it based on `torch.rand` instead of random numbers
                input_tensor = torch.randn(x1.size())
        return input_tensor


# Inputs to the model
x1 = torch.randn(1, 2, 2)
