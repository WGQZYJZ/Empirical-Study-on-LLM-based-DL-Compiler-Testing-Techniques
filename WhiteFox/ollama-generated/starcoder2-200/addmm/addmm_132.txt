
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mul = torch.nn.Linear(10, 1)
 
    def forward(self, x1):
        v2  = torch.mm(x1, inp) # Matrix multiplication of 1st tensor with 'inp' using matmul API
        v3  = v2 + 0  # Adding the result to another tensor 'inp'
        return v3

# Initializing the model
m  = Model()


# Inputs to the model. Note that you don't need to actually create the input tensors for the 1st and 2nd inputs. You may directly provide values such as: [5,6] or 'random_string' which would be a string/value that is not used by the model (just for example).

inp = torch.rand(3) # Tensor of size 3 with uniformly distributed random values.
x1 = [[20,30],[40,50]]  # Size: 2 x 10

