
class Model(torch.nn.Module):
    def __init__(self, embedding_size: int = 64):
        super().__init__()
        self.linear1 = torch.nn.Linear(embedding_size, embedding_size)
 
    def forward(self, x1, x2):
        attn_weights = None

        v1 = x1  # This variable holds the input tensor `x1` before applying the linear transformation `v1`.
        v2 = self.linear1(v1)  # This step computes a vector with the same shape as `x1`, containing the output of the `linear1` transformation applied to `x1`.
        attn_weights = torch.softmax(v2, dim=-1)  # This step applies softmax to these two vectors, and assigns them to an attribute called `attn_weights`.

        v3 = x2  # This variable holds the input tensor `x2` before applying the linear transformation `v3`.
        v4 = self.linear1(v3)  # This step computes a vector with the same shape as `x2`, containing the output of the `linear1` transformation applied to `x2`.
        attn_weights = attn_weights * torch.softmax(v4, dim=-1)  # This step computes the dot product between these two vectors and the attention weights, using a formula similar to the one in the paper.

        output = x2  # The last step assigns the value of `x2` to the first input variable `output`.
        return output


# Initializing the model
m = Model()


