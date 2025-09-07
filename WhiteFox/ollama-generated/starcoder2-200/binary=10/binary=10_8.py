
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):

        # The input tensor
        v1 = torch.randn(20)

        v2  = torch.randn(3)
        v3  = self.linear_layer(v1) # A linear layer with the number of outputs equal to 4

        # Adding a constant value to one of its inputs
        v5  = v3 + v2
 
        return v5


# Initializing the model
m = Model()

# Inputs to the model, which are two tensors of size (3,) and three tensors of shape (10,), respectively.
x1_input = torch.randn(4) # Shape: [3]
x2_inputs  = torch.randn(30).reshape((30, -1)) # Shape: [30, 3]
 
# Running the model on two inputs. Note that each input is a tensor of shape (10,), 
# which means that it has been passed as a batch to the linear layer in the previous step.
__output___  = m(x1_input) # The size of the output of this forward call should be [3] because we have 4 input tensors.
__output____, __output___2  = m(x2_inputs)

