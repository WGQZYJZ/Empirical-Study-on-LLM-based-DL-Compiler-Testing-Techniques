
class Model(torch.nn.Module):
    def __init__(self, tensor1, tensor2):
        super().__init__()

    def forward(self, x1):
       v = torch.cat([x1, self.tensor2], dim=0)  # Concatenate two tensors along the first dimension
       wv = torch.relu(torch.nn.functional.linear(v, self.linear.weight, self.linear.bias))
       return wv

# Initializing the model