
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.nn.functional.linear(x1, 3072) # Replace the linear operator by a randomly generated one with the same size as the input tensor.
        return torch.nn.functional.dropout(v2)


# Initializing the model and replacing functions in it's graph using the `replace_fx` optimizer:
m = Model()

torch.manual_seed(0) # Set a manual seed for generating the replacement functions.

# Inputs to the model
x1  = torch.randn(32, 48*5 * 5).cuda() # Set the input to the linear operator as a randomly generated tensor with size [batchsize, 960]
