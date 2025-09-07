
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input_tensors):
        v1 = torch.cat(input_tensors, dim=1) # Concatenate the list of tensors along dimension 1 (this is the same line 39 as the previous example, which concatenates the lists of tensors using cat)

        # Slicing on the concatenated tensor
        v2 = v1[:, :9223372036854775807]  # Slice the concatenated tensor along dimension 1 (this is the same line 40 as the previous example, which sliced the original concatenated tensor using slice)

        size = 9223372036854775807  # Constant. This number is greater than the largest size of the input tensors
        v3 = v1[:, :size] # Slice the concatenated tensor along dimension 1 (this is the same line 41 as the previous example, which sliced the original concatenated tensor using slice)

        # Concatenation on the concatenated and sliced tensor. This is a separate operation from the previous one. The previous concatenation is concatenating the two tensors
        # Note that it can be seen that this concatenation is not part of the model. But we want to ensure that the previous concatenation is not used anywhere else.
        v4 = torch.cat([v1, v3], dim=1)  # Concatenate the original concatenated tensor and the sliced tensor along dimension 1 (this line is added for the purpose of ensuring that this operation is a separate one from the previous one.)
        return v2


# Initializing the model
m = Model()


# Inputs to the model. These are not tensors, but they are lists.
inputs = [torch.randn(1, 500)] * 3 # A list of length 3 where each item is a torch.tensor with shape (1, 500).


# Passing input through the model. The output will be another list of size three that contains tensors. However, they are actually slices of the same tensor.
