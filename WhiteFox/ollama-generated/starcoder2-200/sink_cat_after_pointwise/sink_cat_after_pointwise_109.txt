
class Model(torch.nn.Module):
    def __init__(self, input1, input2, input3):
        super().__init__()

    def forward(self, x1):
        # Concatenate the inputs with the first dimension = 0.
        v1  = torch.cat([input1, self.weight_1], dim=...)

        # Concatenate the concatenated tensor with the first two dimensions = 0.
        v2  = torch.cat([v1, input2], dim=...)
        
        # Apply a pointwise unary operation after reshaping and concatenation
        # (e.g., ReLU or Tanh). The resulting tensor is then used as a main 
        # input of the linear layer.
        v3  = torch.nn.functional.linear(v2, self.weight_2)
        
        return v3


# Initializing the model