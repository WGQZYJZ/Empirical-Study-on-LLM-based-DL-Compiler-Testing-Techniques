
class Model(torch.nn.Module):
    def __init__(self, key_size):
        super().__init__()
        self.key = torch.nn.Parameter(torch.Tensor([0] * key_size), requires_grad=False)
 
    def forward(self, x1, x2):
        # Calculate the key matrix
        v = x1  # Reshape the input tensor to match with the model
        k = self.key.view(-1, 1, x1.shape[-1])
        scaled_dot_product = torch.matmul(v, k.transpose(-2, -1)) / (math.sqrt(k.shape[-1]))  # Perform the dot product and divide it by the square root of the dimension of the key/query vectors
        attention_weights = scaled_dot_product.softmax(dim=-1)  # Compute softmax on the values with a specified dimension, which is the key_size
        # Calculate the output tensor
        v = x2
        weighted_value = attention_weights.matmul(v)
        return weighted_value


# Initializing the model
m = Model(key_size=64)
x1  = torch.randn(1, 3, 56, 56)
x2 = torch.randn(1, 8, 56, 56)
