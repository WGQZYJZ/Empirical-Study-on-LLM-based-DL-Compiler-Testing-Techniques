
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(4, 2)

    def forward(self, x0: torch.Tensor,
                x1: torch.Tensor) -> torch.Tensor:
        return torch.relu(
            # Reshape the tensor to (3, 2). The optimization `sink_cat_after_pointwise` is triggered because it detects a pattern
            # like `tensor = torch.cat([input_a, input_b], dim=1).view(-1)`. The model should not be this simple, it should contain more operators.
            x0.reshape(3, 2) +
            self.linear2(
                # Apply linear transformation to the reshaped tensor. This is done after concatenation because it should be the only user of the reshaped tensor.
                torch.relu(
                    x1))
        )

# Initializing the model