
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # Permute first input tensor in case it has more than one dimension. 
        v1 = x1.permute(0, -2)
        v3 = torch.bmm(v1, x2)

        return v3


# Initializing the model
m = Model()


# Inputs to the model (tensors x1 and x2 are already present in the previous code snippet)
x1  = torch.randn(10, 64, 785, 98)
x2  = torch.randn(10, 337, 98)

 # Input tensors for each forward call (the model should accept two input tensors).
__input_tensor__ = [None] * 3  # the model should accept three input tensors in total
__input_tensor__[0] = torch.randn(10, 64, 785)
__input_tensor__[1] = torch.randn(10, 98)
__input_tensor__[2] = None

 # Output tensors of each forward call (the model should return one output tensor).
__output_tensors__ = [None] * 3  # the model should return three ouput tensors in total.
__output_tensors__[0] = torch.randn(10, 785)

