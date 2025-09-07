
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, 2) # Input to the linear function is not of shape (n, m), but an input tensor with 3 dimensions. 
        v2 = v1.permute(0, 2, 1)  # The permute method swaps the last two dimensions and outputs a (n, 2, 2) tensor
        return v2


# Initializing the model
m = Model()


# Inputs to the model: 3-d Input with shape of (batch_size x number_of_linear_weights x number_of_output_weights)
x1 = torch.randn(4, 5, 6) # This input is a random tensor. Please also make sure that its shape meets the requirements.

# Outputs from the model
