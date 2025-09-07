
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        # Permute the input tensor so that its last two dimensions are swapped
        v1 = x1.permute(0, 2, 1)

        # Apply dropout to the input tensor
        if self.training:
            v2 = torch.nn.functional.dropout(v1, p=p, training=True)
        else:
            v2 = torch.nn.functional.dropout(v1, p=p, training=False)

        # Generate a tensor with the same size as input_tensor filled with random numbers
        if self.training:
            return torch.rand_like(input_tensor, dtype=torch.float32) * 0.5 + v2
        else:
            return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
