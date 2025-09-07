
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @staticmethod
    def dropout(input_tensor, ...):  # Add a `fallback_random` configuration to `dropout` function
        return torch.nn.functional.dropout(input_tensor, ...)[0]  # Remove the node invoking the `torch.nn.functional.dropout` function and replace it with its replacement (lowmem_dropout)

    @staticmethod
    def randlike(...):  # Add a `fallback_random` configuration to `randlike` function
        return torch.rand_like(...)  # Replace the node invoking the `torch.rand_like` function and replace it with its replacement


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)  # Generates a random tensor of shape (1, 2, 2) in the CPU device
