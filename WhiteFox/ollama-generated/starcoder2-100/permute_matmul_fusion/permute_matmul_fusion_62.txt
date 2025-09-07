
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.permute(x1) # Permute the input tensor x1 
        v2  = torch.permute(x2) # Permute the input tensor x2 (the input tensors)

        if len(v1.shape) < 3:
            # If the permuted tensor is of shape [1, 1], then call the bmm method directly.
            result_tensor = v2 @ v1
        else:
            # Call the bmm function on the two permuted tensors.
            result_tensor = torch.bmm(v1, v2)

        return result_tensor


# Initializing the model
m  = Model()

# Input tensors to this model
x1 = torch.randn(30, 3) # Tensor A (of size [3 x 3]) that gets permuted.
x2 = torch.randn(3, 30) # Tensor B (of size [3 x 30]) that gets permuted.


# Output tensors from the model on the input tensors.
output_1  = m(x1, x2)
output_2  = m(x2, x1)