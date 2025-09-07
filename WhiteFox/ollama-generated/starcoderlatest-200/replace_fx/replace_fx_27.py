
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = input_tensor.permute(...) # Permute the input tensor
        v2 = torch.nn.functional.dropout(v1, 0.5) # Apply dropout to permuted tensor (Note: The graph of this model is the same as the previous one.)
        return v2
