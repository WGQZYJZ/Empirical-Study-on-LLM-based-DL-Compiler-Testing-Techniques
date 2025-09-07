
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.randn(2)  # This line will generate a new input tensor everytime it runs

        v2 = self._permute_and_linear_func_invoke(v1) 
        return v2

    def _permute_and_linear_func_invoke(self, x):
        # Permute the input tensor with more than 2 dimensions
        v1 = x.reshape([3] + [i for i in range(len(x)) if i != -1])

        # Apply linear transformation to the permuted tensor
        w = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model