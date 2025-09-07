
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input_tensor):
        x1  = torch.split(input_tensor, [2,2], dim=0)[0]  # Split the input tensor into two tensors along the 0th dimension
        x2  = torch.cat([x1, x1])                             # Concatenate the first two split tensors along the 0th dimension
        return x2


# Inputs to the model
input_tensor  = torch.randn(3, 64, 64)
__output__  = Model()(input_tensor)

