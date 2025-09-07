
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, inp)
        return v6
 
    # This function is optional
    @classmethod
    def get_input_tensor(cls):
        # Note that the input tensor must be of type Tensor (not torch.Tensor).
        # It cannot be any PyTorch class or variable. Otherwise, there would be a runtime error! 
        # The following function is responsible for returning an instance of an object representing the input tensor.
        return None

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
