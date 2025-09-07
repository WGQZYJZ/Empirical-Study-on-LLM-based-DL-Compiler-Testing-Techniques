# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        return self.linear(x1).permute(0, 2, 1)


# Input tensors for the model
__input__ = input_tensor.permute(0, 2, 1) # Permutation of input tensor from (B, C, H, W) to (C, B, H, W)
