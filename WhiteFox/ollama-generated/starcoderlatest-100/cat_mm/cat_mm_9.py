
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, input2_list):
        v1 = torch.mm(x1, x1)  # The output of the matrix multiplication operation
        v2 = torch.cat([v1, v1] * input2_list[0], dim=0)  # The result tensor is concatenated along dimension=0 (which means "along the first dimension") for the specified times. The length of `input2_list` depends on the desired output dimension
        return torch.cat([v2, v2] * input2_list[1], dim=1)  # The result tensor is concatenated along dimension=1 (which means "along the second dimension") for the specified times. The length of `input2_list` depends on the desired output dimension


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3)  # This tensor is a batch of two tensors with shape (2, 3). The first dimension has no meaning. Its purpose is just for demonstration.
input_list = [2] * 4  # input_list[0] and input_list[1] are used to specify the desired output dimension of the concatenation operation for dimensions "along the first dimension" and "along the second dimension", respectively. For example, if we only want to concatenate a tensor with shape (1, 8) along the first dimension and another tensor with shape (2, 4) along the second dimension: `input_list = [1] * 4`


