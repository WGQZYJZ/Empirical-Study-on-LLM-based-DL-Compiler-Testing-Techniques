
class Model(torch.nn.Module):
    def __init__(self, ):
        super().__init__()

    def forward(self, x1):
        # Input to the model
        x2 = torch.Tensor([0])
        v7  = torch.split(x2, split_sizes=[4], dim=1)

        # Split and concatenate tensors
        v8 = v7[3]

        # Output from the model
        return v8


# Initializing the model
m = Model()


# Inputs to the model
input_tensor  = torch.Tensor([0, 1])
__output__  = m(input_tensor)