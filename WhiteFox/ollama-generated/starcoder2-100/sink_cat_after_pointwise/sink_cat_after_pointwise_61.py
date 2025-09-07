
class Model(torch.nn.Module):
    def __init__(self, num_output):
        super().__init__()
        self.num_output = num_output

    def forward(self, tensor1, tensor2): # tensor 1 and 2 are the tensors to concatenate with. 
        t3 = torch.cat([tensor1, tensor2], dim=0) # Concatenate tensors along a dimension
        t4 = t3.view(-1, self.num_output) # Reshape the concatenated tensor. In this case -1 means unknown dimension. 
        t5 = torch.nn.functional.relu(t4)  # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return t5

m = Model(32)


# Inputs to the model
tensor1 = torch.randn(6, 10) + i
tensor2 = torch.randn(7, 14) - j
