

class Model(torch.nn.Module):
    def __init__(self, input_dim1=None, input_dim2=None):
        super().__init__()

        # Check whether both input dims are None at first
        if (input_dim1 is not None) and (input_dim2 is not None):
            self.linear = torch.nn.Linear(
                in_features=input_dim1 + input_dim2, out_features=3072
            )

    def forward(self, x1, x2):
        v1  = torch.cat([x1, x2], dim=-1) # Concatenate tensors along a dimension
        v2  = v1.view(-1, 5096 * (v1.dim() - 1)) # Reshape the concatenated tensor
        v3 = self.linear(v2) # Apply a pointwise unary operation to the reshaped tensor after concatenation
        return torch.relu(v3), v3


# Initializing the model, with both input dims None at first
m  = Model()


# Inputs to the model that satisfy the model initialization rule above
x1_initial = torch.randn(8, 5096) # Batch size 8, num of elements in the last dimension is 5096 for each tensor
x2_initial = torch.randn(3745, 5096 * (m.linear.in_features - m.linear.out_features))


# Inputs to the model that don't satisfy the model initialization rule above
x1 = torch.randn(8, 5097) # Batch size 8, num of elements in the last dimension is different from 5096 for each tensor x1 and each x2 (first dimension is still equal: 5096)
x2 = torch.randn(3745, 5097 * m.linear.in_features - 5096 * m.linear.out_features) # Batch size 8, num of elements in the last dimension is different from 5096 for each tensor x1 and each x2 (second dimension is still equal: 5097)
