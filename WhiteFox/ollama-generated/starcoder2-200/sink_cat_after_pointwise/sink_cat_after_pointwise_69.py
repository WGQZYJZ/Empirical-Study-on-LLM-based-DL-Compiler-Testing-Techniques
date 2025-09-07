
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
        input = torch.cat([input1, input2], dim=3)  # Concatenate the input tensors along a dimension
        reshaped_tensor = input.view(-1, 50*784)  # Reshape the concatenated tensor
        output = torch.nn.functional.relu(reshaped_tensor, inplace=True)  # Apply a pointwise unary operation (e.g., ReLU or Tanh), using an in-place method to save memory usage.
        return output


# Initializing the model
m = Model()


# Inputs to the model