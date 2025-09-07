
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.functional.conv2d(...) # X can be 1, 2, or 3 representing the dimension of the input tensor.
        bn   = torch.nn.functional.batch_norm(...)
        output = bn(conv(x1))
        return output


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = x1
