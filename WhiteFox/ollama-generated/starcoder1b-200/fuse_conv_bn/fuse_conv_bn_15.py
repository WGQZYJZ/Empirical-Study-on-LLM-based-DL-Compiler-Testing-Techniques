
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    # Functional version of forward function
    @torch.jit._overload_method
    def forward(self, x1):  # In this case 'input_tensor' is a parameter and should match with the pattern described above
        pass

    @torch.jit._overload_method
    def forward(self, input_tensor: torch.Tensor):  # The function name matches with that of forward method
        pass

    def forward(self, x1: Union[Variable, Tensor]):
        conv = torch.nn.functional.conv2d(...)
        bn  = torch.nn.functional.batch_norm(...)

        x2 = conv(x1)
        return bn(x2)


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 4, 5)
