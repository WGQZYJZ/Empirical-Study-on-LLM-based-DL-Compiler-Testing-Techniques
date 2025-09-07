
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, attn_mask, bias=False):
        query  = self.conv(x1) @ x2.transpose(-2, -1)  # Scale the dot product of the input tensors with the weight matrix and compute the square root of the sum of squares
        key = self.conv(x1).transpose(-2, -1)  # Scale the dot product of the input tensors with the weight matrix
        value = x2  # The value tensor is equal to the second input tensor

        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        weighted_sum = (attn_weight @ value) + bias  # Compute the dot product of the attention weights and the value

        return weighted_sum


# Initializing the model
m = Model()


