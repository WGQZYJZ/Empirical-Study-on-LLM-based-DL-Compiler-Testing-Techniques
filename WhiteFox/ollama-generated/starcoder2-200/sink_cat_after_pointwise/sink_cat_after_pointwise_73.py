
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, tensor1, tensor2):
        # Concatenate two tensors along dimension 0 or 1 (e.g., along the batch dimenstion).
        v1 = torch.cat([tensor1, tensor2], 1)

        # Reshape this concatenated tensor.
        v2 = v1.view(-1, 48, 65)
        return torch.nn.functional.tanh(v2)


# Initializing the model