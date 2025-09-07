
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        # Dropout
        # v1 = input_tensor.permute(...)  # Permute the input tensor
        # v2 = torch.nn.functional.dropout(...) # Apply dropout to the permuted tensor
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.dropout(v1, training=self.training, inplace=False)
        # Re-permutation
        # v3 = ...  # Apply re-permutation to the permuted tensor
        return v2


