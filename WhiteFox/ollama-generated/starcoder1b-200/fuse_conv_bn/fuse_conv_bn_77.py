
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        # Input with more than 2 dimensions is transformed to a single input tensor.
        # It swaps the last two dimensions of `x1`. 
        v1 = x1.permute(0, 2, 1)

        # `torch.nn.functional.convXd` and `torch.nn.functional.batch_norm` are used instead of module API equivalents.
        # For more details please check the description of the requirements.
        output  = torch.nn.functional.convXd(v1, self.linear.weight, self.linear.bias)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
