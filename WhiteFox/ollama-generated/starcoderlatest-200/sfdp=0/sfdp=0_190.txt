
class Model(torch.nn.Module):
    def __init__(self, num_heads: int):
        super().__init__()
        self.q = torch.nn.Conv2d(3, 8, kernel_size=1)
        self.k = torch.nn.Conv2d(3, 8, kernel_size=1)
        self.v = torch.nn.Conv2d(3, 8, kernel_size=1)

        self.num_heads = num_heads

    def forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor):
        # Compute the softmax attention weights on the query tensor
        scaled_dot_product  = ...
        attention_weights  = ...
        # Multiply the weighted values of all the heads in the value tensor to get the final output vector
        output = ...

        return output


# Initializing the model
m = Model(num_heads=2)

# Inputs to the model
q = torch.randn(1, 3, 64, 64) # Q must be of size (batch size x number of heads x sequence length x embedding dimension)
k = torch.randn(1, 3, 64, 64) # K must be of size (batch size x number of heads x sequence length x embedding dimension)
v = torch.randn(1, 3, 64, 64) # V must be of size (batch size x number of heads x sequence length x embedding dimension)
